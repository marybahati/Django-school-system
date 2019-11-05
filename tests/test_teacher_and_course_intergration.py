import datetime
from django.test import TestCase
from teacher.models import Teacher
from course.models import Course

class TeacherCourseTestCase(TestCase):
	def setUp(self):
	   self.teacher_a= Teacher.objects.create (
		   first_name = "Mary",
		   last_name = "bahati",
		   date_of_birth = datetime.date(1998,6,10),
		   gender = "female",
		   id_number = "1998",
		   email = "mary@gmail.com",
		   phone_number = "0710464311",
		   subjects_teaching="java",
		   years_of_experience="20",
		   profession="software engineer",
		   county_from="kisii",
		   )
	   self.teacher_b = Teacher.objects.create (
		   first_name = "baha",
		   last_name = "lucky",
		   date_of_birth = datetime.date(1998,6,10),
		   gender = "female",
		   id_number = "1998",
		   email = "lucky@gmail.com",
		   phone_number = "0710464311",
		   subjects_teaching="python",
		   years_of_experience="10",
		   profession="software engineer",
		   county_from="kisii",
		   )
	   self.python= Course.objects.create (
		   name= "python",
		   duration_in_months = 4,
		   start_date=datetime.date(2019,4,3),
		   end_date = datetime.date.today(),
		   description = "web application",
		   )
	   self.htmlcss = Course.objects.create (
		   name= "htmlcss",
		   duration_in_months = 4,
		   start_date=datetime.date(2019,4,3),
		   end_date = datetime.date.today(),
		   description = "Mobile application",
		   )
	   self.java= Course.objects.create (
		   name= "java",
		   duration_in_months = 4,
		   start_date=datetime.date(2019,4,3),
		   end_date = datetime.date.today(),
		   description = "Cyber security",
		   )
	def test_course_can_be_trained_by_a_teacher(self):
	  self.python.teacher = self.teacher_a
	  self.assertEqual(self.python.teacher, self.teacher_a)
	  
	def test_many_courses_can_be_trained_by_one_trainer(self):
	  self.python.teacher = self.teacher_b
	  self.java.teacher = self.teacher_b
	  self.assertEqual(self.java.teacher,self.python.teacher)