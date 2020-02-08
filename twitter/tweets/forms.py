from django import forms
from tweets.models import Tweet, Comment

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(
                attrs = {
                    'id': 'comment-text',
                    'required': True,
                    'placeholder': 'Make a comment!'
                }
            )
        }
