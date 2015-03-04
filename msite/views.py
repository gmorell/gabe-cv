from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import Context,RequestContext
from pages.models import Page

def index(request):
    context = RequestContext(request)
    
    try:
        index_page = Page.objects.get(page_slug="index")
        return redirect('page-view', slug="index", permanent=True)
    except:
        return render_to_response('index_2014_2.html', context)

    
def contact(request):
    context = RequestContext(request)
    return render_to_response('contact_2014_2.html', context)

