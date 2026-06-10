from django.contrib import admin
from .models import Family, Member, ContactInfo


class MemberInline(admin.TabularInline):
    model = Member
    extra = 1
    fields = ('name', 'relation', 'gender', 'date_of_birth', 'education', 'occupation', 'mobile')


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('family_id', 'family_name', 'village', 'gotra', 'mobile', 'member_count', 'created_at')
    list_filter = ('village', 'gotra', 'business', 'is_active')
    search_fields = ('family_name', 'village', 'mobile')
    inlines = [MemberInline]
    list_per_page = 25

    def member_count(self, obj):
        return obj.member_count()
    member_count.short_description = 'Members'


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'family', 'relation', 'gender', 'age', 'education', 'occupation')
    list_filter = ('relation', 'gender', 'family__village')
    search_fields = ('name', 'family__family_name', 'mobile')
    list_per_page = 25


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    pass
