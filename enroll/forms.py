from django import forms

class StudentsRegistration(forms.Form):
    name = forms.CharField()
    Email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()