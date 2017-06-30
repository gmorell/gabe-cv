from rest_framework import serializers
from rest_framework_cache.registry import cache_registry
from rest_framework_cache.serializers import CachedSerializerMixin

from cv.models import Section, Entry
from pages.models import Page
from projects.models import Entry as ProjectEntry
from projects.models import Project, ExternalProjectLink


class NightShiftSerializer(serializers.Serializer):
    enabled = serializers.BooleanField(default=False)


# Pages
class PageSerializer(serializers.ModelSerializer, CachedSerializerMixin):
    class Meta:
        model = Page
        fields = ('nav_icon', 'nav_heading', 'page_heading', 'page_body', 'page_slug')


# CV
class CVEntrySerializer(serializers.ModelSerializer, CachedSerializerMixin):
    related_project = serializers.HyperlinkedModelSerializer()
    class Meta:
        model = Entry
        fields = ('title', 'desc', 'date_start', 'date_end', 'section', 'related_project')


class CVSerializer(serializers.ModelSerializer, CachedSerializerMixin):
    class Meta:
        model = Section
        fields = ('title', 'entries')
    entries = CVEntrySerializer(source="entry_set", many=True)


# Projects
class LinkSerializer(serializers.ModelSerializer, CachedSerializerMixin):
    class Meta:
        model = ExternalProjectLink
        fields = ('url', 'icon')


class EntrySerializer(serializers.ModelSerializer, CachedSerializerMixin):
    class Meta:
        model = ProjectEntry
        fields = ('title', 'slug', 'body', 'posted', 'created', 'modified')


class ProjectSerializer(serializers.ModelSerializer, CachedSerializerMixin):
    entries = EntrySerializer(source="projectentry", many=True)
    links = LinkSerializer(many=True)

    class Meta:
        model = Project
        fields = ('name', 'slug', 'blurb', 'last_updated', 'display_class', 'display_order', 'links', 'entries')


cache_registry(PageSerializer)
cache_registry(CVSerializer)
cache_registry(ProjectSerializer)
cache_registry(EntrySerializer)

