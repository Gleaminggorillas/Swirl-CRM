from django import forms
from .models import Lead

# converts a model into a form
class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        # tuple of fields from .models.Lead
        fields =  (
            'first_name',
            'last_name',
            'age',
            'agent',
        )




class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)