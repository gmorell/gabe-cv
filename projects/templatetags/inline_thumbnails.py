# shamelessly borrowed from http://greenash.net.au/thoughts/2010/06/an-inline-image-django-template-filter/
from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings

#from sorl.thumbnail.main import DjangoThumbnail

from projects.models import InlineEntryImg as IIE

import re

register = template.Library()

regex_inline = re.compile(r'\[img (?P<identifier>[\w]+)( )?(?P<width>[\d]+)?\]')
regex_row_s = re.compile(r'\[row\-s\]')
regex_row_e = re.compile(r'\[row\-e\]')

@register.filter
@stringfilter
def inline_thumbnails(value):
    new_value = value
    it = regex_inline.finditer(value)
    for m in it:
        r = m.groupdict()
        width = r.get('width', 12)
        width_class= "large-%s" % width
        
        try:
            image = IIE.objects.get(identifier=r['identifier'])
            #make this actually work at some point
            #thumbnail = DjangoThumbnail(image.image, (500, 500))
            #new_value = new_value.replace(m.group(), '<img src="%s%s" width="%d" height="%d" alt="%s" /><p><em>%s</em></p>' % ('http://mysite.com', thumbnail.absolute_url, thumbnail.width(), thumbnail.height(), image.title, image.title))
            #
        
            new_value = new_value.replace(m.group(), '<div class="%s columns"><a data-featherlight="%s"><img src="%s" alt="%s" max-width="100%%"/></a><p><em class="caption">%s</em></p></div>' % (width_class, image.image.url, image.image_r.url, image.title, image.title))
        except IIE.DoesNotExist:
            pass
    return new_value


@register.filter
@stringfilter
def inline_article_row_s(value):
    new_value = value
    it = regex_row_s.finditer(value)
    for m in it:
        new_value = new_value.replace(m.group(), '<div class="row">')
        
    return new_value


@register.filter
@stringfilter
def inline_article_row_e(value):
    new_value = value
    it = regex_row_e.finditer(value)
    for m in it:
        new_value = new_value.replace(m.group(), '</div>')
        
    return new_value