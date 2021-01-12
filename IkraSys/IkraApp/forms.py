from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('ikama_number' , 'firstname', 'other_name', 'surname', 'center_id', 'sex', 'course_id')