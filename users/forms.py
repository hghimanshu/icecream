from __future__ import unicode_literals

from django import forms
from django.core.exceptions import ValidationError

from .models import User


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label="Enter email")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields["email"].required = True

    class Meta:
        model = User
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        users = User.objects.filter(email=email)
        if users.exists():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user
