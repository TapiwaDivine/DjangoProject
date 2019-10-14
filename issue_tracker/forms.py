from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Bug


class BugCreationForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        max_length=100, 
        widget=forms.TextInput(
            attrs={
                "id": 'title-input',
                "class": "form-control",
                "placeholder": "Subject",
                "rows": 10,
                "cols": 120
                
            }
        )
    )
    
    content = forms.CharField(
                    label="",
                    widget=forms.Textarea(
                        attrs={
                            "id": "descript-input",
                            "class": "form-control",
                            "placeholder": "Issue Description",
                            "rows": 10,
                            "cols": 200
                            }
                        )
                    )

    class Meta: 
        model = Bug
        fields = ['title', 'content']
        
    def clean_data(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')
        if not title and not content:
            raise forms.ValidationError("Please enter Description")
        