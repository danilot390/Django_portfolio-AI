from datetime import datetime

from apps.projects.models import (
    Project,
    Tag,
    Technology,
    Dataset,
    ProjectContributor,
    ProjectEvaluation,
    TestDB,
    EvaluationMetric,
    ProjectHighlight,
    Category,
)
from apps.core.models import Person
from apps.projects.management.seeds.utils import load_yaml_directory

def upsert_project(project_data):
    defs = project_data['defs']

    project, _ = Project.objects.update_or_create(
        slug = project_data['slug'],
        defaults= defs
    )

    project.tags.set(
        Tag.objects.filter(slug__in=project_data['tags'])
    )

    project.technologies.set(
        Technology.objects.filter(slug__in=project_data['techs'])
    )

    seed_contributors(project, project_data)
    seed_highlights(project, project_data.get('highlights', []))
    seed_evaluations(project, project_data)

    return project

def seed_contributors(project, project_data):
    for contributor in project_data.get('contributors', []):
        person = Person.objects.get(email=contributor['email'])

        ProjectContributor.objects.update_or_create(
            project = project,
            person = person,
            defaults = {
                'role': contributor['role'],
                'contribution': contributor['contribution'],
                'order' : contributor['order'],
            }
        )

def seed_highlights(project, project_data):
    for data in project_data:
        highlight, _ = ProjectHighlight.objects.update_or_create(
            project = project,
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

def seed_evaluations(project, project_data):

    for evaluation_data in project_data.get('evals', []):
        dataset_slug = evaluation_data['dataset'][0]

        dataset = Dataset.objects.get(slug=dataset_slug)

        evaluation, _ = ProjectEvaluation.objects.update_or_create(
            project = project,
            name = evaluation_data['name'],
            defaults = {
                'description': evaluation_data['description'],
                'evaluation_date': datetime.strptime(evaluation_data['evaluation_date'], '%Y-%m-%d').date(),
                'dataset': dataset,
            }
        )

        for test_data in evaluation_data.get('tests',[]):
            test, _ = TestDB.objects.update_or_create(
                project_evaluation = evaluation,
                name = test_data['name'],
                defaults = {
                    'value': test_data['value']
                }
            )

            for metric_data in test_data.get('metrics', []):
                EvaluationMetric.objects.update_or_create(
                    test_db_entry = test,
                    name = metric_data['name'],
                    defaults = {
                        'value': metric_data['value'],
                        'unit': metric_data.get('unit', ''),
                    }
                )

def seed_projects():
    projects_data = load_yaml_directory('projects')
    for project in projects_data:
        upsert_project(project)