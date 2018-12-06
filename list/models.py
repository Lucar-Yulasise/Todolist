from django.db import models

# Create your models here
class ToDu(models.Model):
    title = models.CharField(max_length=23)
    content = models.TextField()
    status = models.CharField(max_length=3)
    create_time = models.DateTimeField(auto_now_add=True)
    accomplish = models.BooleanField(default=False)