# from datetime import datetime

from apps.projects.models import (
    Experience,
    Tag,
    Technology,
    ExperienceHighlight,
    Category,
)
from apps.core.models import Person
from apps.projects.management.seeds.utils import load_yaml_directory

def upsert_experience(experience_data):
    person = Person.objects.get(email=experience_data['email_person'])
    defs = experience_data['defs']

    experience, _ = Experience.objects.update_or_create(
        slug = experience_data['slug'],
        person = person,
        defaults= defs
    )

    experience.tags.set(
        Tag.objects.filter(slug__in=experience_data['tags'])
    )

    experience.technologies.set(
        Technology.objects.filter(slug__in=experience_data['techs'])
    )

    seed_highlights(experience, experience_data.get('highlights', []))

    return experience

def seed_highlights(experience, experience_data):
    for data in experience_data:
        highlight, _ = ExperienceHighlight.objects.update_or_create(
            experience = experience,
            title = data['title'],
            defaults = {
                "summary": "\n".join(data["bullet_points"]),
                "text": " ".join(data["bullet_points"]),
                "impact": data["impact"],
            }
        )

        highlight.categories.set(
            Category.objects.filter(
                slug__in = data.get('categories', [])
            )
        )

def seed_experiences():
    experience_data = load_yaml_directory('experiences')
    for experience in experience_data:
        upsert_experience(experience)