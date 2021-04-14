from django import forms
from django.forms import ModelForm, Textarea, TextInput

from .models import Author, Comments, Post, Subscriber


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "content"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title",
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Short Description",
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Text",
            })
        }


class SubscribeForm(ModelForm):
    author_id = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by("name"),
        empty_label="Choice Author",
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
    )

    class Meta:
        model = Subscriber
        fields = ["email_to", "author_id"]
        widgets = {
            "email_to": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subscriber's Email",
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["comment"]
        widgets = {
            "comment": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Comment",
            }),
        }
