from django.shortcuts import render, redirect
from blog.models import BlogPost, PostComment
from django.views import View
from django.urls import reverse

# Create your views here.


class BlogListView(View):
    def get(self, request, *args, **kwargs):
        blogs = BlogPost.objects.all()
        context = {"blogs": blogs}
        return render(request, "blog/blog_list.html", context)


class BlogDetailView(View):
    def get(self, request, id, *args, **kwargs):
        try:
            blog = BlogPost.objects.get(id=id)
        except:
            return redirect("blogs-list")
        blogs = BlogPost.objects.exclude(id=id)
        return render(
            request, "blog/blog_detail.html", {"blog_data": blog, "blogs": blogs}
        )

    def post(self, request, id, *args, **kwargs):
        try:
            blog = BlogPost.objects.get(id=id)
        except:
            return redirect("blogs-list")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        website = request.POST.get("website")
        message = request.POST.get("message")
        PostComment.objects.create(
            post=blog,
            full_name=full_name,
            email=email,
            message=message,
            website=website,
        )
        return redirect(reverse("blog_detail", kwargs={"id": id}))
