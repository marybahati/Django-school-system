from django.contrib import admin
from.models import Teacher
class TeacherAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","gender","email","subjects_teaching","profession")
    search_fields=("first_name","last_name","subjects_teaching")

admin.site.register(Teacher,TeacherAdmin)

# Register your models here.
