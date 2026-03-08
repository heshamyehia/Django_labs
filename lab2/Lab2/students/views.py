from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from courses.models import Course

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html',
                  {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html',
                  {'student': student})

def student_create(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        email      = request.POST['email']
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        # Enroll in selected courses
        course_ids = request.POST.getlist('courses')
        student.courses.set(course_ids)
        return redirect('student_list')
    return render(request, 'students/student_form.html',
                  {'courses': courses})
