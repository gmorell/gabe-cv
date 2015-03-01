# shamelessly borrowed from http://greenash.net.au/thoughts/2010/06/an-inline-image-django-template-filter/
# but built upon with the love of gabe
from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings

from django.core.urlresolvers import reverse
from docs.models import Document

import re

register = template.Library()

regex = re.compile(r'@(?P<docuuid>[0-9a-f]+)')

@register.filter
@stringfilter
def md_doc_link(value):
    """ Document Link markdown Edition
    """
    new_value = value
    it = regex.finditer(value)
    for m in it:
        r = m.groupdict()
        try:
            doc = Document.objects.get(uuid=r['docuuid'])
            new_value = new_value.replace(m.group(), '[%s](%s) ' % (doc.title,reverse("doc-view", args=(doc.uuid,))))
        except Document.DoesNotExist:
            pass
    return new_value 