from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomePageView.as_view(),name="home-view"),
    path("enroll/<int:id>/",views.CourseEnrollCreateView.as_view(),name="course_enroll"),
    path("contact/us/",views.ContactCreateView.as_view(),name="contact_us"),    
]
