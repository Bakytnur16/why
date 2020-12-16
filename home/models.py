from django.db import models
from django.conf import settings

class Message(models.Model):
  content=models.TextField(max_length=256)
  publish=models.DateTimeField()