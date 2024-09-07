from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    image2 = models.ImageField(upload_to='projects/')
    image3 = models.ImageField(upload_to='projects/')
    image4 = models.ImageField(upload_to='projects/')
    image5 = models.ImageField(upload_to='projects/')

    link = models.URLField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title