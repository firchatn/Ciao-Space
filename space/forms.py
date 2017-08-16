from django import forms
from .models import Post, Message


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'aboutnow')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('body', )
