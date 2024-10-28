from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'age', 'state', 'district', 'mobile_number', 'health_condition']
        widgets = {
            'health_condition': forms.Textarea(attrs={'rows': 4}),
            'mobile_number': forms.TextInput(attrs={'pattern': '[0-9]{10}'}),
        }
