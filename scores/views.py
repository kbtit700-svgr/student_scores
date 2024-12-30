from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Subject, Score
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'scores/index.html', {'students': students, 'subjects': subjects})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    scores = Score.objects.filter(student=student)
    return render(request, 'scores/student_detail.html', {'student': student, 'scores': scores})

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    scores = Score.objects.filter(subject=subject)
    return render(request, 'scores/subject_detail.html', {'subject': subject, 'scores': scores})

def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        student_id = request.POST['student_id']
        Student.objects.create(name=name, student_id=student_id)
        return redirect('index')
    return render(request, 'scores/add_student.html')

def add_score(request):
    if request.method == "POST":
        student_id = request.POST['student']
        subject_id = request.POST['subject']
        score = request.POST['score']
        student = get_object_or_404(Student, pk=student_id)
        subject = get_object_or_404(Subject, pk=subject_id)
        Score.objects.create(student=student, subject=subject, score=score)
        return redirect('index')
    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'scores/add_score.html', {'students': students, 'subjects': subjects})

def add_subject(request):
    if request.method == "POST":
        name = request.POST['name']
        Subject.objects.create(name=name)
        return redirect('index')
    return render(request, 'scores/add_subject.html')

