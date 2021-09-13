from django.db import models

# Create your models here.
class Fight(models.Model):
    style = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateTimeField()