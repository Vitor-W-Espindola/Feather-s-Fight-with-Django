from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fight(models.Model):
    style = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, limit_choices_to={'groups__name':'Authors'})
    
    def __str__(self):
        return "%i -> %s" % (self.id, self.style)
