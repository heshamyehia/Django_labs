from django.shortcuts import render, get_object_or_404, redirect
from .models import Instructor

# LIST all instructors
def instructor_list(request):
    instructors = Instructor.objects.all()  # fetch every row
    return render(request, 'instructors/instructor_list.html',
                  {'instructors': instructors})

# DETAIL for one instructor
def instructor_detail(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)  # 404 if not found
    return render(request, 'instructors/instructor_detail.html',
                  {'instructor': instructor})

# CREATE a new instructor
def instructor_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        email      = request.POST['email']
        bio        = request.POST.get('bio', '')
        Instructor.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            bio=bio
        )
        return redirect('instructor_list')
    return render(request, 'instructors/instructor_form.html')
