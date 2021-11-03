from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from .models import TestAjax

class Regi(ModelForm):
    class Meta:
        model = TestAjax
        fields = ['name','family','age']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 300px;margin:0;height:35px; border: 2px solid green; border-radius:5px',
                'placeholder': 'Name'
                }),
            'family': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 300px;margin:0;height:35px; border: 2px solid green; border-radius:5px',
                'placeholder': 'Family'
                }),
            'age': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 300px;margin:0;height:35px; border: 2px solid green; border-radius:5px',
                'placeholder': 'Age'
                }),
        }