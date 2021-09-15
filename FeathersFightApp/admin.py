from django.contrib import admin

from .models import DeleteRequest, Fight

# Register your models here.
admin.site.register(Fight)
admin.site.register(DeleteRequest)