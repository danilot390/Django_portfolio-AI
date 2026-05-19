from apps.core.models import (
    Profile, Education, ExpertiseGroup,
    Skill, AboutSection, Interest,
)
from .people import seed_me
from apps.projects.management.seeds.utils import load_yaml_data

def seed_profile():

    me = seed_me()
    profile_data = load_yaml_data('profiles.yaml')

    for profile in profile_data.get('profiles',[]):
        prof, _ = Profile.objects.update_or_create(
            person = me,
            defaults = {
                'header': profile.get('header'),
                'summary': profile.get('summary'),
                'active': profile.get('active', False),
                'about_title': profile.get('about_title'),
                'about': profile.get('about'),
            }
        )

        education_data = profile.get('education', [])
        for education in education_data:
            Education.objects.update_or_create(
                profile = prof,
                degree = education['degree'],
                defaults = education,
            )

        skills_data = profile.get('skill_groups', [])
        for group_data in skills_data:
            group, _ = ExpertiseGroup.objects.update_or_create(
                profile = prof,
                group_name = group_data['group_name'],
                defaults={
                    'focus': group_data.get('focus', False)
                }
            )

            for skill in group_data['skills']:
                Skill.objects.update_or_create(
                    expertise = group,
                    name = skill['name'],
                    defaults = skill,
                )
        
        about_section_data = profile.get('about_section', [])
        for about_section in about_section_data:
            AboutSection.objects.update_or_create(
                profile = prof,
                title = about_section['title'],
                defaults={
                    'content' : about_section['content'],
                    'order' : about_section['order'],
                }
            )

        interest_data = profile.get('interests',[])
        for interest in interest_data:
            Interest.objects.update_or_create(
                profile = prof,
                name = interest['name'],
                defaults={
                    'order': interest['order']
                }
            )

