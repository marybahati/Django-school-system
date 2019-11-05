from django.test import TestCase
from .models import Course
import datetime
from teacher.models import Teacher
from course.forms import CourseForm
from django.test import Client
from django.urls import reverse  

class AddCourseTestCase(TestCase):
    def setUp(self):
        self.data={
        "name":"javascript",
        "duration_in_months":6,
        "description":"This is a JavaScript course",
        "end_date":datetime.date(2019,1,1),
        "start_date":datetime.date.today(),
        }
        self.bad_data={
        "name":"JavaScript",
        "duration_in_months":"6",
        "description":"This is a JavaScript course",
        "end_date":datetime.date(1,2,3),
        "start_date":datetime.date.today(),
        "teacher":'Antony Orenge',
        }
    def test_course_form_accepts_valid_data(self):
        form = CourseForm(self.data)
        self.assertTrue(form.is_valid())
    def test_course_form_rejects_invalid_data(self):
        form = CourseForm(self.bad_data)
        self.assertFalse(form.is_valid())  

    def test_add_teacher_view(self):
        client=Client()
        url=reverse("add_course")
        response=client.post(url,self.data)
        self.assertEqual(response.status_code,200) 
  
    def test_add_teacher_view_bad_test(self):
        client=Client()
        url=reverse("add_course")
        response=client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)  

# Create your tests here.
