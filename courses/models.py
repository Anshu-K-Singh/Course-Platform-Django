from django.db import models
import helpers
from cloudinary.models import CloudinaryField

helpers.cloudinary_init()

# Create your models here.

class PublishStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'
    COMING_SOON = 'soon', "coming soon"

class AccessRequired(models.TextChoices):
    ANYONE = 'anyone', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email Required'



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', null=True)
    publish_status = models.CharField(
        max_length=20,
          choices = PublishStatus.choices, 
          default = PublishStatus.DRAFT
          )
    access = models.CharField(max_length=20,
                              choices=AccessRequired.choices,
                              default=AccessRequired.EMAIL_REQUIRED
                              )
    
    @property
    def is_published(self):
        return self.publish_status == PublishStatus.PUBLISHED
    def __str__(self):
        return self.title
    



class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)