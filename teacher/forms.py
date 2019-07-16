from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
	class Meta:
		model= Teacher
		fields='__all__'


# Create your tests here.
