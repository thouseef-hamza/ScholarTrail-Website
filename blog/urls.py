from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blogs-list"),
    path("blog/<int:id>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("blog/<int:id>/comment/", views.CommentCreateView.as_view(), name="blog_comment"),
]
