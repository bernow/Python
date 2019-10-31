from django.shortcuts import render, redirect
from .models import Student

#학생 정보 목록
def index(request):
    students = Student.objects.order_by('-pk')
    return render(request, 'students/index.html', {'students':students})

#학생 정보 입력
def new(request):
    return render(request, 'students/new.html')

#학생 정보 정상적 입력
def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')
    student = Student(name=name, email=email, age=age)
    student.save()

    return redirect('students:detail', student.pk)


#학생 정보 상세 조회
def detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/detail.html', {'student':student})

#학생 정보 삭제
def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('students:index')

def edit(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/edit.html', {'student':student})

def update(request, pk):
    student = Student.objects.get(pk=pk)
    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.age = request.POST.get('age')
    student.save()
    return redirect('students:detail', student.pk)
