from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Students,AttendanceReport

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('ikama_number' , 'firstname', 'other_name', 'surname', 'center_id', 'sex', 'course_id')



class formdegree(forms.ModelForm):
            class Meta:
                model = AttendanceReport
                fields = ('student_id','attendance_id','status')
