from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    c_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    msg = models.TextField(max_length=1000)
    sub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fullname + ' -- '+self.email
    