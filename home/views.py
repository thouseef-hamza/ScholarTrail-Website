from django.shortcuts import render, redirect
from home.models import Thumbnail, Teacher, EnrollCourse, Contact, Course
from blog.models import BlogPost, PostComment
from django.views import View
from home.forms import EnrollNowForm, ContactForm
from django.urls import reverse
from django.http import JsonResponse


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        thumbnails = Thumbnail.objects.all()[:4]
        courses = Course.objects.all()
        teachers = Teacher.objects.all()
        blogs = (
            BlogPost.objects.prefetch_related("blog_comments").all().order_by("-id")[:2]
        )
        form = EnrollNowForm()
        context = {
            "thumbnails": thumbnails,
            "courses": courses,
            "teachers": teachers,
            "form": form,
            "blogs": blogs,
        }
        return render(request, "home/home.html", context)


class CourseEnrollCreateView(View):
    def get(self, request, id, *args, **kwargs):
        course = Course.objects.get(id=id)
        serialized_product = {
            "id": course.pk,
            "course_name": course.course_name,
        }
        return JsonResponse({"data": serialized_product})

    def post(self, request, id, *args, **kwargs):
        forms = EnrollNowForm(request.POST)
        if forms.is_valid():
            try:
                course = Course.objects.get(id=id)
            except Course.DoesNotExist:
                return redirect("home-view")
            EnrollCourse.objects.create(
                course=course,
                full_name=forms.cleaned_data.get("full_name", None),
                email=forms.cleaned_data.get("email", None),
                phone_number=forms.cleaned_data.get("phone_number", None),
            )
            return JsonResponse(
                {
                    "message": "Form Submitted Successfully",
                    "success": True,
                    "status": 201,
                }
            )
        return JsonResponse({"errors": forms.errors, "success": False, "status": 400})

class ContactCreateView(View):
    def post(self, request, *args, **kwargs):
        forms = ContactForm(request.POST)
        if forms.is_valid():
            Contact.objects.create(
                first_name=forms.cleaned_data.get("first_name", None),
                last_name=forms.cleaned_data.get("last_name", None),
                phone_number=forms.cleaned_data.get("phone_number", None),
                message=forms.cleaned_data.get("message", None),
            )
            return JsonResponse(
                {
                    "message": "Form Submitted Successfully",
                    "success": True,
                    "status": 201,
                }
            )
        return JsonResponse({"errors": forms.errors, "success": False, "status": 400})
    
class TeacherDetailView(View):
    def get(self,request,id,*args, **kwargs):
        try:
            teacher=Teacher.objects.get(id=id)
        except:
            return redirect("home-view")
        response_data={
            "id":teacher.id,
            "first_name":teacher.first_name,
            "last_name":teacher.last_name if teacher.last_name else "",
            "profile_picture":teacher.profile_picture.url,
            "position":teacher.position,
            "short_description":teacher.short_description
        }
        return JsonResponse({"data":response_data})
