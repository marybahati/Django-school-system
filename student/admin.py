from django.contrib import admin

from.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display=("registration_number","first_name","last_name","date_of_birth","email","gender","phone_number","date_joined")
	search_fields=("registration_number","first_name","last_name","email","gender","phone_number","date_joined")

admin.site.register(Student,StudentAdmin)


# Register your models here.
