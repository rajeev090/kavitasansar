from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):

    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="")
    content = models.TextField()
    author = models.CharField(max_length=30, default="")
    slug = models.CharField(max_length=150, default="")
    tag = models.CharField(max_length=15, default="")
    date = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return self.title
