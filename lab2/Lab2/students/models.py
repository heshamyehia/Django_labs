from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


from courses.models import Course

class Student(models.Model):
    first_name   = models.CharField(max_length=100)
    last_name    = models.CharField(max_length=100)
    email        = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    enrolled_at  = models.DateTimeField(auto_now_add=True)
    courses      = models.ManyToManyField(
        Course,
        related_name='students'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
