from apps.projects.models import Project, Experience
from apps.core.models import Profile, Person

def get_cv_context():

    person = Person.objects.get(is_me=True)

    profile = person.profile
    experiences = person.experiences.all().order_by('-start_date')
    skills = profile.expertise_groups.all()


    projects = (
        Project.objects
        .all()
    )

    return {
        'person': person,
        'profile': profile,
        'experiences': experiences,
        'projects': projects,
        'skills': skills,
    }