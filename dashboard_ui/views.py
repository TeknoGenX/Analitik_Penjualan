from django.shortcuts import render
from portfolio.models import Project, Comment
from collections import Counter

def dashboard_home(request):
    # Ambil semua project & komentar terbaru (gunakan only untuk efisiensi query)
    projects = Project.objects.only('id', 'title', 'category', 'created_at').order_by('-created_at')
    comments = Comment.objects.select_related('project').only('id', 'name', 'text', 'created_at', 'project').order_by('-created_at')

    # Total data
    total_projects = projects.count()
    total_comments = comments.count()

    # Hitung kategori terbanyak
    category_counts = Counter(projects.values_list('category', flat=True))
    top_categories = sorted(category_counts.items(), key=lambda x: -x[1])[:3]

    # Ambil 5 terbaru
    recent_projects = projects[:5]
    recent_comments = comments[:5]

    return render(request, 'dashboard_ui/dashboard.html', {
        'total_projects': total_projects,
        'total_comments': total_comments,
        'top_categories': top_categories,
        'recent_projects': recent_projects,
        'recent_comments': recent_comments,
    })
