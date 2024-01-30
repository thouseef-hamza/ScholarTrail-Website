from django.db import models

# Create your models here.


class Thumbnail(models.Model):
    title_name = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255, null=True,blank=True)
    background_image = models.ImageField(upload_to="background/")

    def __str__(self) -> str:
        return self.title_name


class Teacher(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="teachers/", default="teachers/teacher.jpg", blank=True
    )
    position = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name + self.last_name


class Course(models.Model):
    course_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="courses/")
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.course_name


class EnrollCourse(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, related_name="course_enrollment", null=True
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.full_name


class Contact(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    contacted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.first_name
