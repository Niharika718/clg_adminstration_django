from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Student, Department, Faculty
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard.html')


def student_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST['email'],
            student_class=request.POST['class'],
            marks=request.POST['marks'],

        )
        return redirect('students')
    return render(request, 'add_student.html')


def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.email = request.POST['email']
        student.student_class = request.POST['class']
        student.marks = request.POST['marks']

        student.save()
        return redirect('students')

    return render(request, 'edit_student.html', {'student': student})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('students')


def department_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})


def add_department(request):
    if request.method == 'POST':
        Department.objects.create(
            name=request.POST['name'],
            code=request.POST['code']
        )
        return redirect('departments')

    return render(request, 'add_department.html')


def edit_department(request, id):
    dept = Department.objects.get(id=id)

    if request.method == 'POST':
        dept.name = request.POST['name']
        dept.code = request.POST['code']
        dept.save()
        return redirect('departments')

    return render(request, 'edit_department.html', {'dept': dept})


def delete_department(request, id):
    dept = Department.objects.get(id=id)
    dept.delete()
    return redirect('departments')


def faculty_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    faculty = Faculty.objects.all()
    return render(request, 'faculty.html', {'faculty': faculty})


def add_faculty(request):
    if request.method == 'POST':
        Faculty.objects.create(
            name=request.POST['name'],
            department=request.POST['department'],
            mobile=request.POST['mobile'],
            email=request.POST['email'],
            doj=request.POST['doj']
        )
        return redirect('faculty')

    return render(request, 'add_faculty.html')

def edit_faculty(request, id):
    f = Faculty.objects.get(id=id)

    if request.method == 'POST':
        f.name = request.POST['name']
        f.department = request.POST['department']
        f.mobile = request.POST['mobile']
        f.email = request.POST['email']
        f.doj = request.POST['doj']
        f.save()
        return redirect('faculty')

    return render(request, 'edit_faculty.html', {'f': f})


def delete_faculty(request, id):
    f = Faculty.objects.get(id=id)
    f.delete()
    return redirect('faculty')




def logout_view(request):
    logout(request)
    return redirect('login')