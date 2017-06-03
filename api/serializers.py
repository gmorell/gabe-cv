from rest_framework import serializers

from cv.models import Section, Entry
from pages.models import Page
from projects.models import Entry as ProjectEntry
from projects.models import Project, ExternalProjectLink


class NightShiftSerializer(serializers.Serializer):
    enabled = serializers.BooleanField(default=False)


# Pages
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('nav_icon', 'nav_heading', 'page_heading', 'page_body', 'page_slug')


# CV
class CVEntrySerializer(serializers.ModelSerializer):
    related_project = serializers.HyperlinkedModelSerializer()
    class Meta:
        model = Entry
        fields = ('title', 'desc', 'date_start', 'date_end', 'section', 'related_project')


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('title', 'entries')
    entries = CVEntrySerializer(source="entry_set", many=True)


# Projects
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalProjectLink
        fields = ('url', 'icon')


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectEntry
        fields = ('title', 'slug', 'body', 'posted', 'created', 'modified')


class ProjectSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(source="projectentry", many=True)
    links = LinkSerializer(many=True)

    class Meta:
        model = Project
        fields = ('name', 'slug', 'blurb', 'last_updated', 'display_class', 'display_order', 'links', 'entries')