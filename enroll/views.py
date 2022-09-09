from django.shortcuts import render
from .forms import StudentsRegistration
# Create your views here.
def showdata(request):
    fm = StudentsRegistration()
    fm.order_fields(field_order=['first_name','last_name','email','name'])
    return render (request, 'enroll/registrationforms.html', {'form':fm})