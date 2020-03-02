from django import forms
from accounts.models import Department,Course,Student


class DepartmentForms(forms.ModelForm):
    class Meta:
        models=Department
        fields="__all__"

class CourseForms(forms.ModelForm):
    class Meta:
        models=Course
        fields="__all__"
class Student(forms.ModelForm):
    class Meta:
        models=Student
        fields="__all__"

