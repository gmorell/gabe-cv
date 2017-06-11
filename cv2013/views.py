import datetime
import json

from django.contrib.syndication.views import Feed
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import HttpResponse
from django.urls import reverse
from django.utils.feedgenerator import SyndicationFeed

from projects.models import Entry, Project


class JSONFeed(SyndicationFeed):
    """
    https://djangosnippets.org/snippets/2859/
    """
    mime_type = "application/json"
    content_type = "application/json"


    def write(self, outfile, encoding):
        data={}
        data.update(self.feed)
        data['items'] = self.items
        json.dump(data, outfile, cls=DjangoJSONEncoder)
        # outfile is a HttpResponse
        if isinstance(outfile, HttpResponse):
            outfile['Access-Control-Allow-Origin'] = '*'

class LatestLogFeed(Feed):
    title = "GMPdotIO Project Feed"
    link = "/log/"
    description = "Log Entries on GMPdotIO"
    author_link = "https://gmp.io"
    author_name = "Gabe"
    author_email = "gmp@gmp.io"
    subtitle = "Terrible Ideas for Terrible People"
    feed_copyright = str(datetime.date.today().year)
    ttl = 600 * 12

    def categories(self):
        return Project.objects.values_list('slug', flat=True)

    def items(self):
        return Entry.objects.order_by('-posted')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.slug

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('log_perma', kwargs={"project":item.project.slug, "slug": item.slug})

class LatestLogFeedJSON(LatestLogFeed):
    feed_type = JSONFeed