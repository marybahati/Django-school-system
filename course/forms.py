from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
	class Meta:
		model= Course
		fields='__all__'

# Create your tests here.
