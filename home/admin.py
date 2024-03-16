from django.contrib import admin
from home.models import Course, Contact, Teacher, Thumbnail, EnrollCourse,Testimonial
from django.utils.html import format_html


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "course_name",
        "image_thumbnail",
        "description",
        "created_at",
        "updated_at",
    )
    search_fields = ("course_name", "description")
    list_filter = ("created_at", "updated_at")

    def image_thumbnail(self, obj):
        return obj.image.url if obj.image else None

    image_thumbnail.short_description = "Image"
    image_thumbnail.allow_tags = True


admin.site.register(Course, CourseAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "message", "contacted")
    list_filter = ("contacted",)
    search_fields = ("first_name", "last_name", "phone_number", "message")
    list_editable = ("contacted",)
    actions = ["mark_as_contacted"]

    def mark_as_contacted(self, request, queryset):
        queryset.update(contacted=True)

    mark_as_contacted.short_description = "Mark selected contacts as contacted"


admin.site.register(Contact, ContactAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "position", "short_description")
    search_fields = ("first_name", "last_name", "position", "short_description")
    list_filter = ("position",)
    list_editable = ("position", "short_description")
    ordering = ("first_name", "last_name")


admin.site.register(Teacher, TeacherAdmin)


class ThumbnailAdmin(admin.ModelAdmin):
    list_display = ("title_name", "sub_title", "display_background_image")
    search_fields = ("title_name", "sub_title")
    list_filter = ("title_name",)

    def display_background_image(self, obj):
        return format_html(
            '<img src="{}" width="50" height="50" />'.format(obj.background_image.url)
        )

    display_background_image.short_description = "Background Image"


admin.site.register(Thumbnail, ThumbnailAdmin)


class EnrollCourseAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone_number",
        "course",
        "enrolled_at",
        "contacted",
    )
    list_filter = ("course", "enrolled_at", "contacted")
    search_fields = ("full_name", "email", "phone_number")


admin.site.register(EnrollCourse, EnrollCourseAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("full_name", "company")
    search_fields = ["full_name", "company"]
    list_filter = ("company",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        return obj.image.url if obj.image else None

    image_preview.short_description = "Image Preview"
    image_preview.allow_tags = True

admin.site.register(Testimonial,TestimonialAdmin)
