from apps.projects.models import Tag, Technology, Category
from apps.projects.management.seeds.utils import load_yaml_data

def seed_tags():
    tags_data = load_yaml_data('tags.yaml')
    for tag in tags_data.get('tags',[]):
        Tag.objects.update_or_create(
            slug=tag['slug'],
            defaults={"name": tag['name']}
        )

def seed_technologies():
    techs_data = load_yaml_data('techs.yaml')
    for tech in techs_data.get('techs', []) :
        Technology.objects.update_or_create(
            slug=tech['slug'],
            defaults={"name": tech['name']}
        )

def seed_categories():
    categories_data = load_yaml_data('categories.yaml')
    for category in categories_data.get('categories', []):
        Category.objects.update_or_create(
            slug=category['slug'],
            defaults={"name": category['name']}
        )