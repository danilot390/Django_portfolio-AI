from apps.projects.models import Dataset
from apps.projects.management.seeds.utils import load_yaml_data

def seed_datasets():
    datasets_data = load_yaml_data('datasets.yaml')
    for dataset in datasets_data.get('datasets',[]):
        Dataset.objects.update_or_create(
            slug=dataset['slug'],
            defaults=dataset
        )