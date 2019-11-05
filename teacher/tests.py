from django.test import TestCase
from .models import Teacher
import datetime
from teacher.forms import TeacherForm
from django.test import Client
from django.urls import reverse      

class AddTeacherTestCase(TestCase):
    def setUp(self):
        self.data={
        "first_name":"Antony",
        "last_name":"Orenge",
        "gender":"male",
        "id_number":"1234",
        "phone_number":"0791863939",
        "email":"antorenge@gmail.com",
        "date_of_birth":datetime.date(1996,12,4),
        "county_from":'Nairobi',
        "subjects_teaching":'JavaScript',
        "years_of_experience":'18',
        "profession":'Software Developer',      
        }
        self.bad_data={
        "first_name":"Antony",
        "last_name":"Orenge",
        "gender":"male",
        "id_number":"1234",
        "phone_number":"07918",
        "email":"antorenge@gmai",
        "date_of_birth":datetime.date(1,2,3),
        "county_from":'Nairobi',
        "subjects_teaching":'JavaScript',
        "years_of_experience":'18',
        "profession":'Software Developer',
        }
    def test_teacher_form_accepts_valid_data(self):
        form = TeacherForm(self.data)
        self.assertTrue(form.is_valid())
    def test_teacher_form_rejects_invalid_data(self):
        form = TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())  

    def test_add_teacher_view(self):
        client=Client()
        url=reverse("add_teacher")
        response=client.post(url,self.data)
        self.assertEqual(response.status_code,200) 

    def test_add_teacher_view_bad_test(self):
        client=Client()
        url=reverse("add_teacher")
        response=client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)                        
        
                                                                                            
# Create your tests here.


# Create your tests here.
