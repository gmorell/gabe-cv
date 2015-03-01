from django.contrib import admin
from docs.models import Document

class DocAdmin(admin.ModelAdmin):
    list_display = ("title",'uuid')

admin.site.register(Document,DocAdmin)