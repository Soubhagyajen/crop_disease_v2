from django.db import models
from django.utils.timezone import now

# class Blog(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True) 

#     class Meta:
#         app_label = 'CropDiseaseDetection'

#     def __str__(self):
#         return self.title
# 
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # If you have 'author', make it optional
    author = models.CharField(max_length=100, blank=True, null=True)  # Optional
    class Meta:
        app_label = 'CropDiseaseDetection'

    def __str__(self):
        return self.title