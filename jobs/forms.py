from django import forms
from django.forms import fields
from . models import Job, Bid


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'budget',
                  'county', 'town', 'status', 'created_by']


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['job', 'technician','amount']
