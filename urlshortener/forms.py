"""""
shortener forms

"""

from django import forms
from django.forms import fields 

from .models import Shortener 

class ShortenerForm(forms.ModelForm):

    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", 'placeholder': "Your URL to shorten"}
    ))

    class Meta:
        model = Shortener

        fields = ('long_url',)