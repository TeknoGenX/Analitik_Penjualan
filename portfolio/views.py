from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Project
from .forms import ProjectForm, CommentForm

def index(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    project_list = Project.objects.all().order_by('-created_at')

    if query:
        project_list = project_list.filter(title__icontains=query)

    if category:
        project_list = project_list.filter(category=category)

    paginator = Paginator(project_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'portfolio/index.html', {
        'projects': page_obj,
        'query': query,
        'category': category,
        'page_obj': page_obj,
    })

def project_detail(request, pk):
    # Optional debug line:
    # print("PK:", pk, type(pk))

    project = get_object_or_404(Project, pk=pk)
    comments = project.comments.order_by('-created_at')
    form = CommentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.project = project
        comment.save()
        return redirect('project_detail', pk=pk)

    return render(request, 'portfolio/detail.html', {
        'project': project,
        'comments': comments,
        'form': form,
    })

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('portfolio_index')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/add_project.html', {'form': form})

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if project.owner != request.user:
        return HttpResponseForbidden()
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project_detail', pk=pk)
    return render(request, 'portfolio/edit_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if project.owner != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio_index')
    return render(request, 'portfolio/delete_project.html', {'project': project})
