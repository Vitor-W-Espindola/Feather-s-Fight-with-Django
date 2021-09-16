from django.contrib import admin

from .models import PublicationRequest, DeleteRequest, EditRequest, Fight

# Register your models here.
admin.site.register(Fight)
admin.site.register(PublicationRequest)
admin.site.register(EditRequest)
admin.site.register(DeleteRequest)