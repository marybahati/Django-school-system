from django.contrib import admin

from.models import Course
class CourseAdmin(admin.ModelAdmin):
    list_display=("name","start_date","end_date","description")
    search_fields=("name","teacher__first_name","teacher__last_name")
		



admin.site.register(Course,CourseAdmin)

# Register your models here.
