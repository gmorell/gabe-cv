# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template import Context,RequestContext

from projects.models import Entry,Project
import datetime,pytz

datetime.datetime.now(pytz.utc)

def log(request,page=1):
    c = {}
    
    now = datetime.datetime.now(pytz.utc)
    e = Entry.objects.filter(posted__lte=now)

    c['entries'] = e
    
    return render(request, 'log_2014.html', c)


def log_perma(request,project,slug,v2014=True):
    c = {}
    
    e = get_object_or_404(Entry,slug=slug)
    c['e'] = e
    
    return render(request, 'log_perma_2014_2.html', c)

def log_project(request,slug):
    c = {}
    
    p = get_object_or_404(Project,slug=slug)
    now = datetime.datetime.now(pytz.utc)
    c['entries'] = p.projectentry.filter(posted__lte=now)
    c['project'] = p
    return render(request, 'log_project_2014.html', c)

def project_list(request):
    c = {}
    p = Project.objects.all()
    c['projects'] = p
    
    return render(request, 'projects_2014_2.html', c)
