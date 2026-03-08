from django.core.management.base import BaseCommand
from instructors.models import Instructor
from courses.models import Course
from students.models import Student
from datetime import date


class Command(BaseCommand):
    help = 'Populate database with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        # Clear existing data
        Student.objects.all().delete()
        Course.objects.all().delete()
        Instructor.objects.all().delete()

        self.stdout.write('Creating instructors...')
        # Create Instructors
        instructors_data = [
            {
                'first_name': 'John',
                'last_name': 'Smith',
                'email': 'john.smith@university.edu',
                'bio': 'Professor of Computer Science with 15 years of experience in software engineering and web development.'
            },
            {
                'first_name': 'Sarah',
                'last_name': 'Johnson',
                'email': 'sarah.johnson@university.edu',
                'bio': 'Data Science expert specializing in machine learning and artificial intelligence.'
            },
            {
                'first_name': 'Michael',
                'last_name': 'Williams',
                'email': 'michael.williams@university.edu',
                'bio': 'Database administrator and expert in SQL, NoSQL, and database design.'
            },
            {
                'first_name': 'Emily',
                'last_name': 'Davis',
                'email': 'emily.davis@university.edu',
                'bio': 'Mobile app development specialist with expertise in iOS and Android platforms.'
            },
            {
                'first_name': 'David',
                'last_name': 'Brown',
                'email': 'david.brown@university.edu',
                'bio': 'Cybersecurity professional teaching network security and ethical hacking.'
            },
        ]

        instructors = []
        for data in instructors_data:
            instructor = Instructor.objects.create(**data)
            instructors.append(instructor)
            self.stdout.write(f'  Created instructor: {instructor}')

        self.stdout.write('Creating courses...')
        # Create Courses
        courses_data = [
            {
                'title': 'Introduction to Python Programming',
                'description': 'Learn the fundamentals of Python programming language, including data types, control structures, functions, and object-oriented programming.',
                'instructor': instructors[0]
            },
            {
                'title': 'Web Development with Django',
                'description': 'Build modern web applications using Django framework. Cover models, views, templates, and deployment.',
                'instructor': instructors[0]
            },
            {
                'title': 'Machine Learning Fundamentals',
                'description': 'Introduction to machine learning algorithms, supervised and unsupervised learning, and practical applications.',
                'instructor': instructors[1]
            },
            {
                'title': 'Data Analysis with Pandas',
                'description': 'Master data manipulation and analysis using Pandas library. Work with real-world datasets.',
                'instructor': instructors[1]
            },
            {
                'title': 'Database Design and SQL',
                'description': 'Learn database design principles, normalization, and SQL query optimization.',
                'instructor': instructors[2]
            },
            {
                'title': 'NoSQL Databases',
                'description': 'Explore MongoDB, Redis, and other NoSQL databases. Understand when to use each type.',
                'instructor': instructors[2]
            },
            {
                'title': 'Mobile App Development',
                'description': 'Build native mobile applications for iOS and Android platforms.',
                'instructor': instructors[3]
            },
            {
                'title': 'React Native Development',
                'description': 'Create cross-platform mobile apps using React Native framework.',
                'instructor': instructors[3]
            },
            {
                'title': 'Network Security',
                'description': 'Understanding network protocols, security threats, and defense mechanisms.',
                'instructor': instructors[4]
            },
            {
                'title': 'Ethical Hacking',
                'description': 'Learn penetration testing techniques and security assessment methodologies.',
                'instructor': instructors[4]
            },
        ]

        courses = []
        for data in courses_data:
            course = Course.objects.create(**data)
            courses.append(course)
            self.stdout.write(f'  Created course: {course.title}')

        self.stdout.write('Creating students...')
        # Create Students
        students_data = [
            {
                'first_name': 'Alice',
                'last_name': 'Anderson',
                'email': 'alice.anderson@student.edu',
                'date_of_birth': date(2002, 5, 15)
            },
            {
                'first_name': 'Bob',
                'last_name': 'Baker',
                'email': 'bob.baker@student.edu',
                'date_of_birth': date(2001, 8, 22)
            },
            {
                'first_name': 'Charlie',
                'last_name': 'Cooper',
                'email': 'charlie.cooper@student.edu',
                'date_of_birth': date(2003, 3, 10)
            },
            {
                'first_name': 'Diana',
                'last_name': 'Martinez',
                'email': 'diana.martinez@student.edu',
                'date_of_birth': date(2002, 11, 5)
            },
            {
                'first_name': 'Ethan',
                'last_name': 'Garcia',
                'email': 'ethan.garcia@student.edu',
                'date_of_birth': date(2001, 7, 18)
            },
            {
                'first_name': 'Fiona',
                'last_name': 'Rodriguez',
                'email': 'fiona.rodriguez@student.edu',
                'date_of_birth': date(2003, 1, 25)
            },
            {
                'first_name': 'George',
                'last_name': 'Wilson',
                'email': 'george.wilson@student.edu',
                'date_of_birth': date(2002, 9, 12)
            },
            {
                'first_name': 'Hannah',
                'last_name': 'Taylor',
                'email': 'hannah.taylor@student.edu',
                'date_of_birth': date(2001, 4, 30)
            },
            {
                'first_name': 'Isaac',
                'last_name': 'Lee',
                'email': 'isaac.lee@student.edu',
                'date_of_birth': date(2003, 6, 8)
            },
            {
                'first_name': 'Julia',
                'last_name': 'White',
                'email': 'julia.white@student.edu',
                'date_of_birth': date(2002, 2, 14)
            },
            {
                'first_name': 'Kevin',
                'last_name': 'Harris',
                'email': 'kevin.harris@student.edu',
                'date_of_birth': date(2001, 10, 3)
            },
            {
                'first_name': 'Laura',
                'last_name': 'Martin',
                'email': 'laura.martin@student.edu',
                'date_of_birth': date(2003, 12, 20)
            },
        ]

        # Create students and enroll them in courses
        for i, data in enumerate(students_data):
            student = Student.objects.create(**data)
            
            # Enroll each student in 2-4 random courses
            if i % 3 == 0:
                student.courses.set([courses[0], courses[2], courses[4]])
            elif i % 3 == 1:
                student.courses.set([courses[1], courses[3], courses[5], courses[7]])
            else:
                student.courses.set([courses[6], courses[8], courses[9]])
            
            enrolled_courses = ', '.join([c.title for c in student.courses.all()])
            self.stdout.write(f'  Created student: {student} - Enrolled in: {enrolled_courses}')

        self.stdout.write(self.style.SUCCESS('\n✓ Database populated successfully!'))
        self.stdout.write(f'  - {len(instructors)} instructors created')
        self.stdout.write(f'  - {len(courses)} courses created')
        self.stdout.write(f'  - {len(students_data)} students created')
