from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from instructors.models import Instructor

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html',
                  {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html',
                  {'course': course})

def course_create(request):
    instructors = Instructor.objects.all()
    if request.method == 'POST':
        title       = request.POST['title']
        description = request.POST.get('description', '')
        instructor_id = request.POST.get('instructor')
        course = Course.objects.create(
            title=title,
            description=description,
            instructor_id=instructor_id or None
        )
        return redirect('course_list')
    return render(request, 'courses/course_form.html',
                  {'instructors': instructors})
