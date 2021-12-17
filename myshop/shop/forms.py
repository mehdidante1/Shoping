from django import forms
from django.forms.widgets import Textarea, Widget



class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    massage = forms.CharField(widget=forms.Textarea)


