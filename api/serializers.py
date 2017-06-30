from django.conf import settings
from rest_framework import serializers
from rest_framework.reverse import reverse

from cv.models import Section, Entry
from pages.models import Page
from projects.models import Entry as ProjectEntry
from projects.models import Project, ExternalProjectLink


class NightShiftSerializer(serializers.Serializer):
    enabled = serializers.BooleanField(default=False)


# Pages
class PageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ('nav_icon', 'nav_heading', 'page_heading', 'page_body', 'page_slug', 'url')

    def get_url(self, obj):
        return settings.SITE_URL + reverse('page-view', (obj.page_slug,))


# CV
class CVEntrySerializer(serializers.ModelSerializer):
    related_project = serializers.HyperlinkedModelSerializer()

    class Meta:
        model = Entry
        fields = ('title', 'desc', 'date_start', 'date_end', 'section', 'related_project')


class CVSerializer(serializers.ModelSerializer):
    entries = CVEntrySerializer(source="entry_set", many=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = ('title', 'entries', 'url')

    def get_url(self, obj):
        return settings.SITE_URL + reverse('cv_index')


# Projects
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalProjectLink
        fields = ('url', 'icon')


class EntrySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = ProjectEntry
        fields = ('title', 'slug', 'body', 'posted', 'created', 'modified', 'url')

    def get_url(self, obj):
        return settings.SITE_URL + reverse('log_perma', args=[obj.project.slug, obj.slug])


class ProjectSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(source="projectentry", many=True)
    links = LinkSerializer(many=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('name', 'slug', 'blurb', 'last_updated', 'display_class', 'display_order', 'links', 'entries', 'url')

    def get_url(self, obj):
        return settings.SITE_URL + reverse('log_project', (obj.slug,))
