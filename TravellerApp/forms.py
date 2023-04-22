from .models import Trip, Comment
from django import forms
from utils.constants import TAGS


class TripForm(forms.ModelForm):
    """
    trip creator/editor form
    """
    tags = forms.MultipleChoiceField(
      choices=TAGS,
      widget=forms.CheckboxSelectMultiple()
      )

    class Meta:
        model = Trip
        fields = (
            'title',
            'author',
            'featured_image',
            'budget',
            'route',
            'accommodation',
            'guide',
            'additional_info',
        )
    

class CommentForm(forms.ModelForm):
    """
    Form to post public comments to trips
    """
    commenting = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
          'body': 'Write a comment'
        }
        widgets = {
          'body': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
        }

