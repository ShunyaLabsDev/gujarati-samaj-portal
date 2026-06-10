from django import forms
from families.models import Family, Member
from events.models import Event
from announcements.models import Announcement


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['family_name', 'village', 'gotra', 'address', 'mobile', 'email', 'business', 'family_photo']
        widgets = {
            'family_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'કુટુંબ નામ / Family Name'}),
            'village': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ગામ / Village'}),
            'gotra': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '98765 43210'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'business': forms.Select(attrs={'class': 'form-select'}),
            'family_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'relation', 'gender', 'date_of_birth', 'education', 'occupation', 'mobile', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'નામ / Name'}),
            'relation': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'event_date', 'event_time', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'publish_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'publish_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
