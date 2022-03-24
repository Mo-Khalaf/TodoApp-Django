from dataclasses import fields
from turtle import title
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields='__all__'
