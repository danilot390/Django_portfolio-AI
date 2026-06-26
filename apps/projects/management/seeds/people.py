from apps.core.models import Person, SocialLink, Language
from apps.projects.management.seeds.utils import load_yaml_data

PEOPLE_DATA = load_yaml_data('people.yaml') or {}

def _save_links(person, links):
    for link in links:
        SocialLink.objects.update_or_create(
            person=person,
            platform=link['platform'],
            defaults={
                'url': link['url'],
                'order': link.get('order', 0),
            }
        )

def _save_languages(person, languages):
    for language in languages:
        Language.objects.update_or_create(
            person=person,
            name=language['name'],
            defaults={
                'proficiency': language.get('proficiency', 'basic'),
                'order': language.get('order', 0),
            }
        )

def seed_me():
    me = PEOPLE_DATA.get('me')
    if not me:
        print('Me data is necessary in `people.yaml`.')
        return None
    
    person, _ = Person.objects.update_or_create(
        email=me['email'],
        defaults={
            "name":me['name'], 
            'phone_number': me['phone_number'],
            "is_me": True,
        },
    )

    _save_links(person, me.get('social_links', []))

    if 'languages' in me:
        _save_languages(person, me['languages'])
        
    return person

def seed_collaborators():
    collaborators = PEOPLE_DATA.get('people', [])

    for data in collaborators:
        person, _ = Person.objects.update_or_create(
                email = data['email'],
                name = data['name'],
            )
        
        _save_links(person, data['social_links'])
        
        if 'languages' in data:
            _save_languages(person, data['languages'])