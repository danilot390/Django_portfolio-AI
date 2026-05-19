from django.db import models
from django.db.models import Q

class Person(models.Model):
    name = models.CharField(max_length=100)
    
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True)

    is_me = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return self.name
    
    @property
    def linkedin_url(self):
        link = self.social_links.filter(platform='linkedin').first()
        return link.url if link else None

    @property
    def github_url(self):
        link = self.social_links.filter(platform='github').first()
        return link.url if link else None


class SocialLink(models.Model):
    person =models.ForeignKey(Person,related_name='social_links', on_delete=models.CASCADE, null=True)
    
    platform = models.CharField(max_length=50)
    url = models.URLField( max_length=300)
    
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.platform
    
    class Meta:
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(
                fields=['person', 'platform'],
                name='unique_plataform_per_person'
            )
        ]
class Profile(models.Model):
    person = models.OneToOneField(Person, related_name='profile', on_delete=models.CASCADE)
    
    header = models.CharField(max_length=150)
    summary = models.TextField(blank=True)
    
    about_title = models.CharField(max_length=150)
    about = models.TextField()
    
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.person.name} Profile"
    
    @property
    def focus_expertise_groups(self):
        """Allows access via profile.expertise_groups"""
        return self.expertise_groups.filter(focus=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['person'],
                condition = Q(active=True),
                name = 'unique_active_profile_per_person',
            )
        ]

class AboutSection(models.Model): 
    profile = models.ForeignKey(Profile, related_name='abouts', on_delete=models.CASCADE)
    
    title = models.CharField( max_length=150)
    content = models.TextField()
    
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['order']

class Interest(models.Model):
    profile = models.ForeignKey(Profile, related_name='interests', on_delete=models.CASCADE)
    
    name = models.CharField( max_length=150)
    
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(
                fields=['profile','name'],
                name = 'unique_interest_per_profile'
            )
        ]


class Education(models.Model):
    profile = models.ForeignKey(Profile, related_name='educations', on_delete=models.CASCADE)
    
    degree = models.CharField(max_length=150)
    institution = models.CharField( max_length=150)
    graduation = models.CharField( max_length=150)
    span = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return f'{self.degree} - {self.institution}'
    
    class Meta:
        ordering = ['graduation']

class ExpertiseGroup(models.Model):
    profile = models.ForeignKey(Profile, related_name='expertise_groups', on_delete=models.CASCADE)
    
    group_name = models.CharField(max_length=100)
    focus = models.BooleanField(default=False)
    
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.group_name
    
    @property
    def focus_skills(self):
        """Allows access via expertise.active_skills"""
        return self.skills.filter(focus=True)
    
    class Meta:
        ordering = ['order',]

class Skill(models.Model):
    expertise = models.ForeignKey(ExpertiseGroup, related_name='skills', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=3)
    
    focus = models.BooleanField(default=False)
    
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order',]
        constraints = [
            models.UniqueConstraint(
                fields=['expertise', 'name'],
                name='unique_skill_per_expertise',
            )
        ]


