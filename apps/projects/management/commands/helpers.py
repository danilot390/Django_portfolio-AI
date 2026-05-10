from datetime import datetime

from apps.projects.models import (
    Project, Tag, Technology, Category,
    ProjectContributor, Dataset, ProjectEvaluation, 
    TestDB, EvaluationMetric, ProjectHighlight
)
from apps.core.models import (
    Person, Profile, Education,
    ExpertiseGroup, Skill
)

from django.contrib.auth import get_user_model


def admin_user(self):
    User = get_user_model()
    # Admin user
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'password')
        self.stdout.write(self.style.SUCCESS('Admin user created. Username: admin, Password: password'))
    else:
        self.stdout.write('Admin user already exists.')

def first_seed(self):
    # Person 
    me, _ = Person.objects.get_or_create(
        name='Danilo Angel Tito Rodriguez', 
        defaults={
            'email':'danilot390@gmail.com',
            'linkedin_url':'https://www.linkedin.com/in/danilo-tito-7313931a7',
            'github_url':'https://github.com/danilot390',

            'is_me': True
            })
    
    # Tags
    tags=[
        ['Artificial Intelligence', 'ai'],
        ['Machine Learning', 'ml'],
        ['Spiking Neural Networks', 'snn'],
        ['Convolutional Neural Networks', 'cnn'],
        ['XGBoost', 'xgboost'],
        ['Green AI', 'green-ai'],
        ['Explainable AI', 'xai']
    ]
    for name, slug in tags:
        Tag.objects.get_or_create(name=name, slug=slug)
    self.stdout.write(self.style.SUCCESS('Tags created.'))

    # Categories
    categories = [
        ("Architecture", "architecture"),
        ("Performance", "performance"),
        ("Efficiency", "efficiency"),
        ("Deployment", "deployment"),
    ]
    for name, slug in categories:
        Category.objects.get_or_create(name=name, slug=slug)
    self.stdout.write(self.style.SUCCESS('Categories created.'))

    # Technologies
    techs = [
        ['Python', 'python'],
        ['Django', 'django'],
        ['PyTorch', 'pytorch'],
        ['Scikit-learn', 'sklearn'],
        ['XGBoost', 'xgboost'],
        ['SHAP', 'shap'],
        ['LIME', 'lime'],
        ['SNN-Torch', 'snntorch'],
        ['SpikingJelly', 'spikingjelly'],
        ['CodeCarbon', 'codecarbon']
    ]
    for name, slug in techs:
        Technology.objects.get_or_create(name=name, slug=slug)
    self.stdout.write(self.style.SUCCESS('Technologies created.'))

    # Dataset
    datasets = [
        {
            'name': 'Credit Card Fraud Detection',
            'slug': 'CCFD-ULB',
            'author': 'Machine Learning Group (ULB)',
            'description': 'A dataset containing transactions made by credit cards in September 2013 by European cardholders. The dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions.',
            'source_url': 'https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud',
            'num_rows': 284807,
            'num_features': 31
        },
        {
            'name': 'Synthetic Financial Datasets For Fraud Detection',
            'slug': 'SFDFD-PaySim',
            'author': 'EDGAR LOPEZ-ROJAS',
            'description': 'A collection of synthetic financial datasets designed for fraud detection research, covering various transaction types and fraud scenarios.',
            'source_url': 'https://www.kaggle.com/datasets/kaggle/synthetic-financial-datasets-for-fraud-detection',
            'num_rows': 6362620,
            'num_features': 13
        }
    ]
    for data in datasets:
        Dataset.objects.get_or_create(name=data['name'], defaults=data)
    self.stdout.write(self.style.SUCCESS('Datasets created.'))

    # Create a sample project
    projects = [
        {
            'title': 'Green-AI Fraud Detection System',
            'defs':{
                    'slug': 'green-ai-fraud-detection',
                    'description': ('A  novel hybrid Deep Learning project to combat financial fraud. It combines spiking neural networks (SNNs)'
                                    ' for ultra-efficient initial pattern detection with Multi Layer Perceptron and staking meta-learner XGBoost,'
                                    ' and incorporates Explainable AI (XAI) techniques. This approach delivers reductions in energy consumption, '
                                    'while maintaining high accuracy and providing interpretable results.'),
                    'short_description': ('This project proposes a novel neuromorphic-inspired hybrid fraud detection framework (SNN+MLP-XGBoost) that integrates '
                                    'Green AI metrics and explainablity mechanism, supported by empirical evidence demonstrating improved '
                                    'sustainability with competitive predictive performance.'),
                    'is_featured': True,
                    'is_published': False,
                    'github_url': 'https://github.com/danilot390/Green-Ai-Fraud-Detection',
                    'complexity': 7
                    },
            'tags': [
                'ai','ml', 'snn', 'cnn', 'xgboost', 'green-ai', 'xai'
                ],
            'techs':[
                'python','pytorch', 'sklearn', 'xgboost', 'lime', 'codecarbon', 'snntorch', 'spikingjelly'
            ],
            'highlights': [
                {
                    'title': 'Energy Efficient Hybrid Fraud Detection',
                    'bullet_points': [
                        'Improved detection performance through complementary model strengths',
                        'Reduced computational overhead via efficient model components',
                        'Balanced predictive performance with energy efficiency (Green AI principles)',
                    ],
                    'impact': 'High Accuracy with reduced energy consumption.',
                    'categories': ['architecture', 'efficiency']
                },{
                    'title': 'Performance Improvement via Hybrid Approach',
                    'bullet_points': [
                        'Improved classification performance over individual models',
                        'Enhanced robustness to class imbalance (Critical in fraud detection).',
                        'Captured temporal dynamics (SNNs) and static relationships (MLPs/XGBoost) in data.',
                        'Reduced false positives and false negatives via meta-learning.'
                    ],
                    'impact': 'More reliable fraud detection in imbalanced datasets.',
                    'categories': ['performance', 'efficiency']
                },{
                    'title': 'Scalable Production-Ready ML System',
                    'bullet_points': [
                        'End-to-end ML pipeline from data processing to ddeployment.',
                        'Modular architecture suppporting independent model updates.',
                        'Supports explainability, monitoring, drift detection, and retraining.',
                        'High scalability and extensibility.'
                    ],
                    'impact': 'Follows the best practices for production-ready ML systems.',
                    'categories': ['deployment']
                }
            ],
            'evals':[
                {
                    'name': 'Performance Evaluation',
                    'description': ('The results indicate that the proposed Green Hybrid Model achieves the strongest overall balance '
                                    'between precision and recall, yielding the highest F1-Score, f2-Score, and PR-AUC among all'
                                    'evaluated models. This demostrates that combining temporal modelling with static feature learining'
                                    'improves fraud detection effectivness compared with others architectures.'),
                    'evaluation_date': '2025-12-07',
                    'dataset': ['CCFD-ULB'],
                    'tests': [
                        {
                            'name': 'MLP',
                            'value': 1,
                            'metrics': [
                                {'name': 'Recall', 'value': 0.8108, 'unit': ''},
                                {'name': 'PR-AUC', 'value': 0.8242, 'unit': ''},
                                {'name': 'F1-Score', 'value': 0.7317, 'unit': ''},
                                {'name': 'F2-Score', 'value': 0.7772, 'unit': ''},
                            ]
                        },{
                            'name': 'XGBoost/MLP/BiLSTM',
                            'value': 2,
                            'metrics': [
                                {'name': 'Recall', 'value': 0.8082, 'unit': ''},
                                {'name': 'PR-AUC', 'value': 0.7819, 'unit': ''},
                                {'name': 'F1-Score', 'value': 0.8082, 'unit': ''},
                                {'name': 'F2-Score', 'value': 0.8016, 'unit': ''},
                            ]
                        },{
                            'name': 'Hybrid Green',
                            'value': 3,
                            'metrics': [
                                {'name': 'Recall', 'value': 0.8108, 'unit': ''},
                                {'name': 'PR-AUC', 'value': 0.8382, 'unit': ''},
                                {'name': 'F1-Score', 'value': 0.8633, 'unit': ''},
                                {'name': 'F2-Score', 'value': 0.8310, 'unit': ''},
                            ]
                        },
                    ]
                },{
                    'name': 'Green AI Evaluation',
                    'description': ('The outcomes reflect that while MLP model are the most computationally lightweight,'
                                    'proposed model achieves a favoruable balance between efficiency and predictive power. '
                                    'The sustainability results show that model complexity correlates with environmental cost.'),
                    'evaluation_date': '2025-12-07',
                    'dataset': ['CCFD-ULB'],
                    'tests': [
                        {
                            'name': 'MLP',
                            'value': 1,
                            'metrics': [
                                {'name': 'Infer. Latency', 'value': 0.1847, 'unit': 'MS'},
                                {'name': 'Flops', 'value': 0.0000, 'unit': 'GFlops'},
                                {'name': 'Size', 'value': 0.1846, 'unit': 'MB'},
                                {'name': 'Energy', 'value': 0.0010, 'unit': 'kWh'},
                            ]
                        },{
                            'name': 'XGBoost/MLP/BiLSTM',
                            'value': 2,
                            'metrics': [
                                {'name': 'Infer. Latency', 'value': 0.9993, 'unit': 'MS'},
                                {'name': 'Flops', 'value': 0.8194, 'unit': 'GFlops'},
                                {'name': 'Size', 'value': 0.8082, 'unit': 'MB'},
                                {'name': 'Energy', 'value': 0.0024, 'unit': 'kWh'},
                            ]
                        },{
                            'name': 'Hybrid Green',
                            'value': 3,
                            'metrics': [
                                {'name': 'Infer. Latency', 'value': 0.9996, 'unit': 'MS'},
                                {'name': 'Flops', 'value': 0.9231, 'unit': 'GFlops'},
                                {'name': 'Size', 'value': 0.8101, 'unit': 'MB'},
                                {'name': 'Energy', 'value': 0.0017, 'unit': 'kWh'},
                            ]
                        },
                    ]
                },{
                    'name': "Ileberi & Sun's Model",
                    'description': ("By mimic the Ilibery & Sun's models and compare the results on the same data splits,"
                                    'the differences between performance and effectivness are notoriuos inclining heavily '
                                    'into the proposed model, reflecting the advantages on conbining SNNs and MLPs for Fraud '
                                    'detection systems.'),
                    'evaluation_date': '2025-12-27',
                    'dataset': ['CCFD-ULB'],
                    'tests': [
                        {
                            'name': 'I&S Model-Baseline',
                            'value': 1,
                            'metrics': [
                                {'name': 'Recall', 'value': 0.7973, 'unit': ''},
                                {'name': 'PR-AUC', 'value': 0.4078, 'unit': ''},
                                {'name': 'F1-Score', 'value': 0.5990, 'unit': ''},
                                {'name': 'F2-Score', 'value': 0.7041, 'unit': ''},
                                {'name': 'Latency', 'value': 22.7381, 'unit': 'MS'},
                            ]
                        },{
                            'name': 'I&S Model-Tuned',
                            'value': 2,
                            'metrics': [
                                {'name': 'Recall', 'value': 0.8378, 'unit': ''},
                                {'name': 'PR-AUC', 'value': 0.4651, 'unit': ''},
                                {'name': 'F1-Score', 'value': 0.6596, 'unit': ''},
                                {'name': 'F2-Score', 'value': 0.7561, 'unit': ''},
                                {'name': 'Latency', 'value': 17.5324, 'unit': 'MS'},
                            ]
                        },{
                            'name': 'Hybrid Green',
                            'value': 3,
                            'metrics': [
                                {'name': 'Recall', 'value': 0.8108, 'unit': ''},
                                {'name': 'PR-AUC', 'value': 0.8382, 'unit': ''},
                                {'name': 'F1-Score', 'value': 0.8633, 'unit': ''},
                                {'name': 'F2-Score', 'value': 0.8310, 'unit': ''},
                                {'name': 'Latency', 'value': 0.9996, 'unit': 'MS'},
                            ]
                        },
                    ]
                }
            ]
        }
    ]

    for pdata in projects:
        project, created = Project.objects.get_or_create(
            slug=pdata['defs']['slug'],
            defaults={
                'title': pdata['title'],
                'description': pdata['defs']['description'],
                'short_description': pdata['defs']['short_description'],
                'is_featured': pdata['defs']['is_featured'],
                'is_published': pdata['defs']['is_published'],
                'github_url': pdata['defs']['github_url'],
                'complexity': pdata['defs']['complexity'],
            }
        )

        if not created:
            project.title = pdata['title']
            project.description = pdata['defs']['description']
            project.short_description = pdata['defs']['short_description']
            project.is_featured = pdata['defs']['is_featured']
            project.is_published = pdata['defs']['is_published']
            project.github_url = pdata['defs']['github_url']
            project.complexity = pdata['defs']['complexity']
            project.save()

        project.tags.set(Tag.objects.filter(slug__in=pdata['tags']))
        project.technologies.set(Technology.objects.filter(slug__in=pdata['techs']))

        ProjectContributor.objects.get_or_create(
            project=project,
            person=me,
            defaults={
                'role': 'Lead Researcher',
                'contribution': 'Project design, experimentation and implementation.',
                'order': 1,
            }
        )

        for highlight_data in pdata['highlights']:
            highlight, _ = ProjectHighlight.objects.get_or_create(
                project=project,
                title=highlight_data['title'],
                defaults={
                    'summary': '\n'.join(highlight_data['bullet_points']),
                    'text': ' '.join(highlight_data['bullet_points']),
                    'impact': highlight_data['impact'],
                }
            )
            highlight.categories.set(
                Category.objects.filter(slug__in=highlight_data.get('categories', []))
            )

        for evaluation_data in pdata['evals']:
            dataset_slug = evaluation_data['dataset'][0] if evaluation_data.get('dataset') else None
            dataset = Dataset.objects.filter(slug=dataset_slug).first() if dataset_slug else None
            if not dataset:
                continue

            evaluation, _ = ProjectEvaluation.objects.get_or_create(
                project=project,
                name=evaluation_data['name'],
                defaults={
                    'description': evaluation_data['description'],
                    'evaluation_date': datetime.strptime(evaluation_data['evaluation_date'], '%Y-%m-%d').date(),
                    'dataset': dataset,
                }
            )
            evaluation.description = evaluation_data['description']
            evaluation.evaluation_date = datetime.strptime(evaluation_data['evaluation_date'], '%Y-%m-%d').date()
            evaluation.dataset = dataset
            evaluation.save()

            for test_data in evaluation_data.get('tests', []):
                testdb, _ = TestDB.objects.get_or_create(
                    project_evaluation=evaluation,
                    name=test_data['name'],
                    defaults={'value': test_data['value']}
                )
                testdb.value = test_data['value']
                testdb.save()

                for metric_data in test_data.get('metrics', []):
                    EvaluationMetric.objects.get_or_create(
                        test_db_entry=testdb,
                        name=metric_data['name'],
                        defaults={
                            'value': metric_data['value'],
                            'unit': metric_data.get('unit', ''),
                        }
                    )

        self.stdout.write(self.style.SUCCESS(f"Seeded project: {project.title}"))

def profile_seed(self):
    # Person 
    me, _ = Person.objects.get_or_create(
        name='Danilo Angel Tito Rodriguez', 
        defaults={
            'email':'danilot390@gmail.com',
            'linkedin_url':'https://www.linkedin.com/in/danilo-tito-7313931a7',
            'github_url':'https://github.com/danilot390',

            'is_me': True
            })
    
    profile_data = {
        'header': 'AI Engineer | Machine Learning | Backend Systems.',
        'defs': {
            'summary': ("I am a mathematics enthusiast with a degree in Software Engineering, currently transitioning into Artificial Intelligence through an MSc in AI in Ireland. I bring over four years of experience, I've built real-world web systems for government institutions, universities, and private clients, focusing on delivering scalable and reliable solutions.\n"
                        "My work combines software engineering expertise with AI, where I am building experience through projects involving end-to-end pipelines, from data preprocessing and model development to basic deployment and monitoring, following MLOps principles and engineering best practices.\n"
                        "I have hands-on experience with TensorFlow, PyTorch, and scikit-learn, and I'worked across Machine Learning, Reinforcement Learning, and hybrid AI architectures . I enjoy building modular, production-oriented systems with strong focus on evaluation, monitoring,a nd reproducibility.\n"
                        "I am particularly interested in Green AI, applying techniques such as pruning, quantization, and energy tracking to build efficient and sustainable AI systems."),
            'active': True
        }
    }
    
    profile, _ = Profile.objects.get_or_create(
        person = me,
        header = profile_data['header'],
        defaults={
            'summary': profile_data['defs']['summary'],
            'active': profile_data['defs']['active']
        }
    )
    self.stdout.write(self.style.SUCCESS(f"Seeded profile: {profile}"))

    education_data = [
        {
            'degree': 'MSc in Artificial Intelligence',
            'institution': 'National College of Ireland',
            'graduation': 'In progrss, expected 2026',
        },{
            'degree': 'BSc in Software Engineering',
            'institution': 'Universidad Autónoma Tomás Frías',
            'graduation': '2021',
            'span': 'Honours',
        },
    ]
    for education in education_data:
        Education.objects.get_or_create(
            profile = profile,
            degree = education['degree'],
            institution = education['institution'],
            graduation = education['graduation'],
        )

    self.stdout.write(self.style.SUCCESS(f"Seeded ({len(education_data)}) education"))

    skills_data=[
        {
            'group_name':'Machine Learning & AI',
            'skills':[
                'Supervised learning, feature engineering, model evaluation',
                'Reinforcement Learning (MDPs, Q-learning)',
                'Hybrid AI systems, Explainable AI (LIME)',
                'TensorFlow, PyTorch, scikit-learn',
                'Green AI: pruning, quantization, energy-aware pipelines   ',
            ],
        },{
            'group_name':'Data Analytics',
            'skills':[
                'Data preprocessing, EDA, and visualization',
                'Statistical analysis and hypothesis testing',
                'Pandas, NumPy, Matplotlib, and Seaborn',
            ],
        },{
            'group_name':'Backend & Systems',
            'skills':[
                'Django, Flask, Laravel',
                'RESTful API design and development',
                'Node.js (JavaScript Runtime)',
                'Microservices Systems',
            ],
        },{
            'group_name':'Databases & Tools',
            'skills':[
                'PostgreSQL, MySQL, SQLite',
                'Git, Docker, CI/CD Pipelines',
                'MLflow, Energy Tracking Tools',
            ],
        },
    ]
    for skills in skills_data:
        expertise_group, _ = ExpertiseGroup.objects.get_or_create(
                                profile=profile,
                                group_name = skills['group_name']
                            )
        for skill in skills['skills']:
            Skill.objects.get_or_create(
                expertise = expertise_group,
                name = skill
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded skill ({expertise_group.group_name}) - {len(skills['skills'])} skills."))

    