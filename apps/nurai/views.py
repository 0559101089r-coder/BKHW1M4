from django.shortcuts import render
import apps.nurai.models as Student

# Create your views here.

def index(request):
    students = Student.Student.objects.all()
    return render(request, 'index.html', locals())