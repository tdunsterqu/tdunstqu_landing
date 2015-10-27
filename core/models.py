from django.db import models

# Create your models here.
class Message(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  message = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

