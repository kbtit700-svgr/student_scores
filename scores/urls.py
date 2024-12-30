from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('subject/<int:pk>/', views.subject_detail, name='subject_detail'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_score/', views.add_score, name='add_score'),
    path('add_subject/', views.add_subject, name='add_subject'),

]
