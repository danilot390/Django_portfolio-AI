from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    
    email = models.EmailField(unique=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    is_me = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    person = models.ForeignKey(Person, related_name='profile', on_delete=models.CASCADE)
    header = models.CharField(max_length=150)
    summary = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.person.name} Profile"

class Education(models.Model):
    profile = models.ForeignKey(Profile, related_name='educations', on_delete=models.CASCADE)
    degree = models.CharField(max_length=150)
    institution = models.CharField( max_length=150)
    graduation = models.CharField( max_length=150)
    span = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return f'{self.degree} - {self.institution}'

class ExpertiseGroup(models.Model):
    profile = models.ForeignKey(Profile, related_name='expertise_groups', on_delete=models.CASCADE)
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name

class Skill(models.Model):
    expertise = models.ForeignKey(ExpertiseGroup, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


