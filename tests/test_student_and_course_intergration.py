from django.test import TestCase
from student.models import Student 
from course.models import Course
import datetime
# from teacher.models import Teacher
# from course.forms import CourseForm
# from django.test import Client
# from django.urls import reverse  

class StudentCourseTestCase(TestCase):

	def setUp(self):
		self.student_a=Student.objects.create(
			first_name="Mary",
			last_name="Bahati",
			date_of_birth=datetime.date(2000, 3, 30),
			gender="female",
			registration_number="001",
			email="baha@gmail.com",
			phone_number="0728287616",
			date_joined=datetime.date.today(), 
			
			    
			)

		self.student_b=Student.objects.create(
			first_name="Sam",
			last_name="Ndirangu",
			date_of_birth=datetime.date(1996, 2, 18),
			gender="Male",
			registration_number="009",
			email="Sam@gmail.com",
			phone_number="0704436849",
			date_joined=datetime.date.today(), 
			

			          
			)

		self.python=Course.objects.create(
			name="python",
			duration_in_months=6,
			description="This is a python course",
			end_date=datetime.date(2019,1,1),
			start_date=datetime.date.today(),            
			)

		self.javascript=Course.objects.create(
			name="javascript",
			duration_in_months=10,
			description="This is a JavaScript course",
			end_date=datetime.date(2018,2,1),
			start_date=datetime.date.today(),            
			)

		self.java=Course.objects.create(
			name="java",
			duration_in_months=5,
			description="This is a java course",
			end_date=datetime.date(2019,3,1),
			start_date=datetime.date.today(),            
			)




	def test_student_can_join_a_course(self):
		self.student_a.courses.add(self.python)
		self.assertEqual(self.student_a.courses.count(),1)
		
	def test_student_can_join_many_courses(self):
		self.student_b.courses.add(self.python,self.javascript,self.java)
		self.assertEqual(self.student_b.courses.count(),3)	