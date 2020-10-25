from .models import UserRating
from django import forms


class RatingForm(forms.ModelForm):
    class Meta:
        model = UserRating
        fields = '__all__'
        exclude = ['book', 'user']
