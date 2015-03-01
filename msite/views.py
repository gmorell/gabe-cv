from django.shortcuts import render_to_response
from django.template import Context,RequestContext

def index(request):
    context = RequestContext(request)
    
    return render_to_response('index.html', context)
    
def index_2014(request):
    context = RequestContext(request)
    
    return render_to_response('index_2014_2.html', context)

    
def contact(request):
    context = RequestContext(request)
    return render_to_response('contact.html', context)

def contact_2014(request):
    context = RequestContext(request)
    return render_to_response('contact_2014_2.html', context)