from django.contrib import admin
from .models import (
    Person, Profile, Education,
    EducationModule, EducationFocusArea, Language,
    ExpertiseGroup, Skill, SocialLink,
    AboutSection, Interest,
    )
from apps.projects.models import Experience

class ExperienceInLine(admin.TabularInline):
    model = Experience
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
class ExpertiseInline(admin.TabularInline):
    model = ExpertiseGroup
    extra = 0
    show_change_link = True
class SocialLinkInLine(admin.TabularInline):
    model = SocialLink
    extra = 1
    show_change_link = True

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0
    max_num = 1
    can_delete = False
    show_change_link = True

class AboutSectionInline(admin.TabularInline):
    model = AboutSection
    extra = 0

class InterestInline(admin.TabularInline):
    model = Interest
    min_num = 2
    extra = 0

class LanguageInLine(admin.TabularInline):
    model = Language
    extra = 1
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_me')
    search_fields = ('name', 'email')
    list_filter = ('is_me',)
    ordering = ('name',)
    inlines = [ProfileInline, SocialLinkInLine, ExperienceInLine, LanguageInLine]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('person', 'header')
    search_fields = ('person__name', 'header')
    inlines = [EducationInline, ExpertiseInline, AboutSectionInline, InterestInline]

class EducationModuleInline(admin.TabularInline):
    model = EducationModule
    extra = 1

class EducationFocusAreaInLine(admin.TabularInline):
    model = EducationFocusArea
    extra = 1
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'graduation')
    search_fields = ('degree', 'institution')
    ordering = ('-graduation',)
    inlines = [EducationModuleInline, EducationFocusAreaInLine]

@admin.register(ExpertiseGroup)
class ExpertiseGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'profile')
    search_fields = ('group_name',)
    inlines = [SkillInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'expertise')
    search_fields = ('name',)
    ordering = ('name',)
