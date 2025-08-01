from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='portfolio_index'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/add/', views.add_project, name='add_project'),
    path('project/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('project/<int:pk>/delete/', views.delete_project, name='delete_project'),
]
