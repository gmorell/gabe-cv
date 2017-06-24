from adminsortable.admin import SortableAdmin
from django.contrib import admin

from projects.models import Project, ExternalProjectLink, Entry, InlineEntryImg


class ProjectLinkInline(admin.StackedInline):
    model = ExternalProjectLink
    
    
class ProjectAdmin(SortableAdmin):
    list_display = ('name', 'slug', 'last_updated', 'display_class','parent')
    inlines = [ProjectLinkInline,]
    
    
class IIEAdmin(admin.ModelAdmin):
    list_display = ('title','identifier')
    
    
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title','project','posted')
    list_filter = ('project','posted')
    prepopulated_fields = {"slug":("title",)}
    
    
admin.site.register(Project,ProjectAdmin)
admin.site.register(ExternalProjectLink)
admin.site.register(Entry,EntryAdmin)
admin.site.register(InlineEntryImg,IIEAdmin)