from django.db import models
import uuid
from django.conf import settings

class Post(models.Model):
    memo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    memo = models.TextField()
    date = models.DateField(auto_now=True, editable=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
