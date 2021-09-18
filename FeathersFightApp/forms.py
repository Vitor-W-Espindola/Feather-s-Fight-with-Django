# forms.py
from django.forms import ModelForm
from .models import PublicationRequest

class PublicationRequestForm(ModelForm):
    class Meta:
        model = PublicationRequest
        fields = ['text']

