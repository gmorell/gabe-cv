from django.db import models
from uuidfield import UUIDField

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    
    uuid = UUIDField(auto=True)
    in_index = models.BooleanField(default=False)
    
    