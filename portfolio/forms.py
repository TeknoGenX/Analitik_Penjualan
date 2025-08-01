from django import forms
from .models import Project, Comment

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['owner', 'created_at']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
