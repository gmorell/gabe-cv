from django.db import models
import uuid

# Create your models here.
from django.db.models.fields import UUIDField


class Document(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    
    uuid = models.UUIDField(default=uuid.uuid4)
    in_index = models.BooleanField(default=False)
    
    