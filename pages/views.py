from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context,RequestContext

from pages.models import Page

def page(request, slug):
    c = RequestContext(request)
    
    p = get_object_or_404(Page, page_slug=slug)
    c['content'] = p
    
    return render_to_response('page.html', c)
