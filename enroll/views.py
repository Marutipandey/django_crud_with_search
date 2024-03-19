# enroll/views.py
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm 
from django.shortcuts import render, redirect, get_object_or_404

# def home(request):
#     students = Student.objects.all()
#     return render(request, "enroll/index.html", {'data': students})
def home(request):
    query = request.GET.get('search')
    if query:
        students = Student.objects.filter(stuname__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, "enroll/index.html", {'data': students})
    
def postdatainform(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')   
    else:
        form = StudentForm()
    
    if request.GET.get('search'):
        quertset = Student.objects.filter(stuname__icontains =request.GET.get('search'))


    students = Student.objects.all()  
    return render(request, 'enroll/index.html', {'form': form, 'data': students})

def studelete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')


def stuedit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'enroll/editpage.html', {'form': form})

# def stusearch(request):
#     query = request.GET.get('q')
#     if query:
#         students = Student.objects.filter(stuname__icontains=query)
#     else:
#         students = Student.objects.all()
#     return render(request, 'enroll/index.html', {'data': students})

