from django.contrib import admin
from .models import Course
from django.utils.html import format_html
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_status', 'access')
    list_filter =["publish_status", "access"]
    fields = ["title", "description", "publish_status", "access", "display_image"]
    readonly_fields = ["display_image"]

    def display_image(self, obj):
        url = obj.image.url
        return format_html('<img src="{}" width="500"/>'.format(url))

