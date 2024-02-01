from django.contrib import admin
from blog.models import BlogPost, PostComment

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title_name",
        "created_at",
        "updated_at",
    )
    search_fields = ["title_name"]
    list_filter = [
        "created_at",
        "updated_at",
    ]
    date_hierarchy = "created_at"
    prepopulated_fields = {"title_name": ("title_name",)}


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "website", "created_at")
    list_filter = ("created_at",)
    search_fields = ("full_name", "email", "website", "message")
    date_hierarchy = "created_at"
    readonly_fields = (
        "created_at",
    ) 
    ordering = ("-created_at",)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(PostComment,PostCommentAdmin)
