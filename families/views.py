from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from .models import Family, Member, ContactInfo
from events.models import Event
from announcements.models import Announcement
from gallery.models import GalleryImage
from django.utils import timezone


def home(request):
    """Home page with community overview"""
    total_families = Family.objects.filter(is_active=True).count()
    total_members = Member.objects.filter(is_active=True).count()

    upcoming_events = Event.objects.filter(
        event_date__gte=timezone.now().date()
    ).order_by('event_date')[:3]

    announcements = Announcement.objects.filter(
        is_published=True
    ).order_by('-publish_date')[:4]

    gallery_preview = GalleryImage.objects.order_by('-created_at')[:6]

    contact = ContactInfo.objects.first()

    context = {
        'total_families': total_families,
        'total_members': total_members,
        'upcoming_events': upcoming_events,
        'announcements': announcements,
        'gallery_preview': gallery_preview,
        'contact': contact,
    }
    return render(request, 'public/home.html', context)


def family_directory(request):
    """Vasti Patrak - Family Directory with search/filter"""
    families = Family.objects.filter(is_active=True).prefetch_related('members')

    search = request.GET.get('search', '')
    village = request.GET.get('village', '')
    gotra = request.GET.get('gotra', '')
    business = request.GET.get('business', '')

    if search:
        families = families.filter(
            Q(family_name__icontains=search) |
            Q(village__icontains=search)
        )
    if village:
        families = families.filter(village__icontains=village)
    if gotra:
        families = families.filter(gotra=gotra)
    if business:
        families = families.filter(business=business)

    # Sort
    sort = request.GET.get('sort', 'family_name')
    if sort == 'village':
        families = families.order_by('village', 'family_name')
    else:
        families = families.order_by('family_name')

    paginator = Paginator(families, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get unique villages for filter dropdown
    villages = Family.objects.filter(is_active=True).values_list('village', flat=True).distinct().order_by('village')

    from .models import GOTRA_CHOICES, BUSINESS_CHOICES

    context = {
        'page_obj': page_obj,
        'search': search,
        'village': village,
        'gotra': gotra,
        'business': business,
        'villages': villages,
        'gotra_choices': GOTRA_CHOICES,
        'business_choices': BUSINESS_CHOICES,
        'total_count': families.count(),
        'sort': sort,
    }
    return render(request, 'public/family_directory.html', context)


def family_detail(request, pk):
    """Family details page"""
    family = get_object_or_404(Family, pk=pk, is_active=True)
    members = family.members.filter(is_active=True).order_by('relation')
    return render(request, 'public/family_detail.html', {'family': family, 'members': members})


def family_pdf(request, pk):
    """Export family details as PDF"""
    family = get_object_or_404(Family, pk=pk, is_active=True)
    members = family.members.filter(is_active=True).order_by('relation')

    # Simple HTML-based PDF using browser print
    context = {'family': family, 'members': members}
    return render(request, 'public/family_pdf.html', context)


def contact_page(request):
    """Contact information page"""
    contact = ContactInfo.objects.first()
    return render(request, 'public/contact.html', {'contact': contact})
