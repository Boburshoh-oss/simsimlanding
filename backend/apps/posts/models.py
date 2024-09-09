from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    image2 = models.ImageField(upload_to='projects/',blank=True,null=True)
    image3 = models.ImageField(upload_to='projects/',blank=True,null=True)
    image4 = models.ImageField(upload_to='projects/',blank=True,null=True)
    image5 = models.ImageField(upload_to='projects/',blank=True,null=True)

    link = models.URLField(max_length=255,blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title