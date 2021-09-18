from django.contrib import admin

from .models import PublicationRequest, Fight, SavePublication

# Register your models here.
admin.site.register(Fight)
admin.site.register(SavePublication)
admin.site.register(PublicationRequest)
