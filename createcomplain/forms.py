from django import forms
from .models import Comment,comaplain

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')


class ComplainForm(forms.ModelForm):
    class Meta:
        model = comaplain
        fields = ["title", "content","status"] 

class ComplainFormadmin(forms.ModelForm):
    class Meta:
        model = comaplain
        fields = ["title", "content","status"]         