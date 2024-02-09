from django.db import models

# Create your models here.





class BlogPost(models.Model):
    title_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogs/")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title_name


class PostComment(models.Model):
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="blog_comments"
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="comments/", default="user-dummy.png", blank=True
    )
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title_name


