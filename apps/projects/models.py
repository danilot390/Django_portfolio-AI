from django.db import models
from apps.core.models import Person

class NamedModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Tag(NamedModel):
    pass

class Technology(NamedModel):
    pass

class Category(NamedModel):
    pass

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    complexity = models.IntegerField(default=1)

    short_description = models.TextField()
    description = models.TextField(blank=True)
    highlights = models.TextField(blank=True)

    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    github_url = models.URLField(blank=True)
    report_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField('Tag', blank=True, related_name='projects')
    technologies = models.ManyToManyField('Technology', blank=True, related_name='projects')

    def __str__(self):
        return self.title
    
    def full_stars(self):
        return self.complexity // 2

    def has_half_star(self):
        return self.complexity % 2 != 0
    
class ProjectHighlight(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_highlights')
    
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    text = models.TextField(blank=True)

    impact = models.CharField(max_length=100, blank=True)
    categories = models.ManyToManyField("Category", blank=True, related_name='highlights')

    def bullet_points(self):
        return [line.strip() for line in self.summary.split('\n') if line.strip()]
    
    def __str__(self):
        return f'Highlight for {self.project.title}: {self.text[:50]}...'
    
class ProjectContributor(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributors')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='contributions')

    role = models.CharField(max_length=100, blank=True)
    contribution = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.person.name} - {self.role} in {self.project.title}'
    
    class Meta:
        unique_together = ('project', 'person')
        ordering = ['order']

class Dataset(models.Model):
    name = models.CharField( max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True)
    source_url = models.URLField(blank=True)

    num_rows = models.IntegerField(blank=True, null=True)
    num_features = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} by {self.author} - {self.num_rows} rows, {self.num_features} features'

class ProjectEvaluation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='evaluations')
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE,blank=True, related_name='evaluations')

    name = models.CharField(blank=True, max_length=50)
    description = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    evaluation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Evaluation for {self.project.title} - Description: {self.description}"
    
class TestDB(models.Model):
    project_evaluation = models.ForeignKey(ProjectEvaluation, on_delete=models.CASCADE, related_name='testdb_entries')
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return f'{self.name}: {self.value}'
  
class EvaluationMetric(models.Model):
    test_db_entry = models.ForeignKey(TestDB, on_delete=models.CASCADE, related_name='metrics', null=True, blank=True)
    
    name = models.CharField(max_length=50)
    value = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=20, blank=True)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}: {self.value} {self.unit}'

class EvaluationConfiguration(models.Model):
    evaluation = models.ForeignKey(
        ProjectEvaluation, on_delete=models.CASCADE, related_name='configurations')
    
    parameters = models.JSONField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.evaluation.project} : {self.parameters}'
