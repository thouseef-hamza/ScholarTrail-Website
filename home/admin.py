from django.contrib import admin
from home.models import Course, Contact, Teacher, Thumbnail, EnrollCourse

# Register your models here.
admin.site.register(Course)
admin.site.register(Contact)
admin.site.register(Teacher)
admin.site.register(Thumbnail)
admin.site.register(EnrollCourse)

