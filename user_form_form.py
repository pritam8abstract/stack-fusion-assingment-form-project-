from django import forms
from django.forms import DateInput
from .models import UserForm

class UserFormForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'})
        }

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get
