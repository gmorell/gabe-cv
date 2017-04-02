from django.shortcuts import get_object_or_404, render
from django.template import Context,RequestContext

from pages.models import Page

def page(request, slug):
    p = get_object_or_404(Page, page_slug=slug)
    c = {"content": p}

    return render(request, 'page.html', c)
