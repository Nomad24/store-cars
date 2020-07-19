from django import forms
from .models import Car
import re
from django.core.exceptions import ValidationError


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["title", "slug", "author", "content", "photo", "category", "price",]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control rows 5"}),
            "photo": forms.FileInput(attrs={"class": "form-control-file"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('The name must not start with a number')
        return title

