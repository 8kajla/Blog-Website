from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['post']
        labels = {"user_name": "Name:","email":"Email I'd:","text":"Comment:"}
