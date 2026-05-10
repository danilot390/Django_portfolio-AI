from django.contrib import admin
from .models import (
    Project,
    ProjectContributor,
    Tag,
    Technology,
    ProjectEvaluation,
    Dataset,
    TestDB,
    EvaluationMetric,
    ProjectHighlight,
    EvaluationConfiguration
)

class ProjectContributorInline(admin.TabularInline):
    model = ProjectContributor
    extra = 1
    autocomplete_fields = ['person']
    show_change_link = True

class ProjectHighlightInline(admin.TabularInline):
    model = ProjectHighlight
    extra = 1
    autocomplete_fields = ['project']


class ProjectEvaluationInline(admin.TabularInline):
    model = ProjectEvaluation
    extra = 0
    show_change_link = True

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'order', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'short_description')
    list_filter = ('created_at', 'updated_at', 'tags', 'technologies', 'is_featured', 'is_published')

    inlines = [ProjectContributorInline, ProjectEvaluationInline, ProjectHighlightInline]

    prepopulated_fields = {'slug': ('title',)}

    autocomplete_fields = ['tags', 'technologies']

    ordering = ('order', '-created_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_rows', 'num_features', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('num_rows', 'num_features')

class EvaluationMetricInline(admin.TabularInline):
    model = EvaluationMetric
    extra = 1

class TestDBInline(admin.TabularInline):
    model = TestDB
    extra = 0

@admin.register(ProjectEvaluation)
class ProjectEvaluationAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'evaluation_date')
    search_fields = ('project__title', 'name', 'description')
    list_filter = ('evaluation_date', 'project')

    inlines = [TestDBInline]

    autocomplete_fields = [ 'project']

@admin.register(TestDB)
class TestDbAdmin(admin.ModelAdmin):
    list_display = ('project_evaluation', 'name', )

    inlines = [EvaluationMetricInline]