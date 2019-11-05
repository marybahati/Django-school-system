from django.test import TestCase
from .models import Student
import datetime
from course.models import Course
from django.core.exceptions import ValidationError
from student.forms import StudentForm
from django.test import Client
from django.urls import reverse

class StudentTestCase(TestCase):
    def setUp(self):
        self.student=Student(
            first_name='Mary',
            last_name='Bahati',
            date_of_birth=datetime.date(2000, 3, 30),
            gender='female',
            registration_number='001',
            email='baha@gmail.com',
            phone_number='0728287616',
            date_joined=datetime.date.today(), 
            )
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name, self.student.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name())

    def test_age_is_always_above_17(self):
       self.assertFalse(self.student.clean() < 17 )
    def test_age_is_always_below_30(self):
       self.assertFalse(self.student.clean() > 30)        

class AddStudentTestCase(TestCase):
    def setUp(self):
        self.data={
        "first_name":"Mary",
        "last_name":"Bahati",
        "gender":"female",
        "registration_number":"1234",
        "phone_number":"0791863939",
        "email":"mary@gmail.com",
        "date_of_birth":datetime.date(1996,12,4),
        "date_joined":datetime.date.today(),        }
        self.bad_data={
        "first_name":"1234",
        "last_name":"4876",
        "gender":"female",
        "registration_number":"1234",
        "phone_number":"abcd",
        "email":"marbaha",
        "date_of_birth":datetime.date(1,2,3),
        "date_joined":datetime.date.today(),
        }
    def test_student_form_accepts_valid_data(self):
        form = StudentForm(self.data)
        self.assertTrue(form.is_valid())
    def test_student_form_rejects_invalid_data(self):
        form = StudentForm(self.bad_data)
        self.assertFalse(form.is_valid()) 
    def test_add_student_view(self):
        client=Client()
        url=reverse("add_student")
        response=client.post(url,self.data)
        self.assertEqual(response.status_code,200) 

    def test_add_student_view_bad_test(self):
        client=Client()
        url=reverse("add_student")
        response=client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)                           
        
                                                                                            
# Create your tests here.
