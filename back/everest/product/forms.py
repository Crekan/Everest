from django import forms
from django.forms import ModelForm, TextInput
from .models import *


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email', 'text')
