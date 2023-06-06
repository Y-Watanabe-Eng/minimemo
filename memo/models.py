from django.db import models
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    memo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    memo = models.TextField()
    date = models.DateTimeField(auto_now_add=True, editable=True)
