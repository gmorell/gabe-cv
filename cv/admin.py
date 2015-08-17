from django.contrib import admin
from cv.models import *
#from pagedown.widgets import AdminPagedownWidget

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title','section','related_project','show_in_pdf')
    #formfield_overrides = {
        #models.TextField: {'widget': AdminPagedownWidget },
    #}

admin.site.register(Section)
admin.site.register(Entry,EntryAdmin)