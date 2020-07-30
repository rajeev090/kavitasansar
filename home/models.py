from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):

    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15, default="")
    msgtype = models.CharField(max_length=15, default="")
    message = models.TextField()
    date = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return 'From: ' + self.name + ' - ' + self.email + ' ' + (f' {self.date}'[0:20])
