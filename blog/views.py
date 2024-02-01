from django.shortcuts import render, redirect
from blog.models import BlogPost, PostComment
from django.views import View
from blog.forms import CommentForm
from django.http import JsonResponse


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
        form = CommentForm()
        return render(
            request,
            "blog/blog_detail.html",
            {"blog_data": blog, "blogs": blogs, "form": form},
        )
class CommentCreateView(View):
    def post(self, request, id, *args, **kwargs):
        print(request   )
        try:
            blog = BlogPost.objects.get(id=id)
        except BlogPost.DoesNotExist:
            return JsonResponse(
                {"errors":" User Not Exist", "success": False, "status": 400}
            )
        forms = CommentForm(request.POST)
        if not forms.is_valid():
            return JsonResponse(
                {"errors": forms.errors, "success": False, "status": 400}
            )
        PostComment.objects.create(
            post=blog,
            full_name=forms.cleaned_data.get("full_name", None),
            email=forms.cleaned_data.get("email", None),
            message=forms.cleaned_data.get("message", None),
            website=forms.cleaned_data.get("website", None),
        )
        return JsonResponse(
            {"message": "Comment Created Successfully", "success": True, "status": 201}
        )

