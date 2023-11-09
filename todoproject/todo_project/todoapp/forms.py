from django import forms
from .models import task


class updateform(forms.ModelForm):
    class Meta:
        model=task
        fields=['taskname','taskpriority','taskdate']
