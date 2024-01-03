from django import forms
from .models import Feedback
from django.core.exceptions import ValidationError

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):  # Пример валидации
            raise forms.ValidationError('Пожалуйста, введите корректный адрес электронной почты.')
        return email


