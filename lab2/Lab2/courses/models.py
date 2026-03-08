from django.db import models
from instructors.models import Instructor

class Course(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructor  = models.ForeignKey(
        Instructor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='courses'
    )
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_image_filename(self):
        """Return the image filename based on course title keywords"""
        title_lower = self.title.lower()
        
        if 'python' in title_lower:
            return 'pylogo.jpg'
        elif 'web' in title_lower or 'django' in title_lower or 'html' in title_lower or 'css' in title_lower:
            return 'webdev.webp'
        elif 'machine learning' in title_lower or 'ml' in title_lower or 'ai' in title_lower:
            return 'ML.webp'
        elif 'data' in title_lower or 'analytics' in title_lower:
            return 'data-analysis.svg'
        elif 'database' in title_lower or 'sql' in title_lower:
            return 'database.svg'
        elif 'mobile' in title_lower or 'android' in title_lower or 'ios' in title_lower:
            return 'mobile.svg'
        elif 'security' in title_lower or 'cyber' in title_lower:
            return 'security.svg'
        else:
            return 'default.svg'
