from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Student
    path('students/', views.student_list, name='students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

    # Department
    path('departments/', views.department_list, name='departments'),
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/edit/<int:id>/', views.edit_department, name='edit_department'),
    path('departments/delete/<int:id>/', views.delete_department, name='delete_department'),

    # Faculty
    path('faculty/', views.faculty_list, name='faculty'),
    path('faculty/add/', views.add_faculty, name='add_faculty'),
    path('faculty/edit/<int:id>/', views.edit_faculty, name='edit_faculty'),
    path('faculty/delete/<int:id>/', views.delete_faculty, name='delete_faculty'),

    # Logout
    path('logout/', views.logout_view, name='logout'),
]