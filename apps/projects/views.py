import json
import numpy as np
from django.shortcuts import render, get_object_or_404

from .models import Project

def projects(request):

    projects = (
        Project.objects
        .prefetch_related('tags', 'technologies')
        .order_by('-is_featured', 'order', '-created_at')
        ) 

    context = {
        'projects': projects,
    }
    return render(request, 'projects/projects.html', context)

def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects.prefetch_related(
            'tags',
            'technologies',
            'contributors',
            'evaluations__dataset',
            'evaluations__testdb_entries__metrics'
        ),
        slug=slug
    )

    evaluations = project.evaluations.all()

    chart_data = []
    for eval in evaluations:
        test_data = []
        for test in eval.testdb_entries.all():
            metrics = {m.name: float(m.value) if m.value is not None else None for m in test.metrics.all()}
            test_data.append({
                'name': test.name,
                'metrics': metrics
            })

        chart_data.append({
            'name': eval.name,
            'description': eval.description,
            'dataset': eval.dataset.name if eval.dataset else None,
            'comment': eval.comment,
            'tests': test_data,
        })

    context = {
        'project': project,
        'evaluations': evaluations,
        'chart_data': json.dumps(chart_data),
    }
    return render(request, 'projects/project_detail.html', context)
