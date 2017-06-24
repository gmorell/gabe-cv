# Create your views here.
import datetime
import pytz

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from projects.models import Entry, Project

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

    # This is a really ugly hack. :(
    c['entries'] = Entry.objects.filter(Q(project=p)|Q(project__parent=p)|Q(project__parent__parent=p)).filter(posted__lte=now)
    # c['entries'] = p.projectentry.filter(posted__lte=now)
    c['project'] = p
    c['children'] = p.children.all()
    return render(request, 'log_project_2014.html', c)

def project_list(request):
    c = {}
    p = Project.objects.filter(parent__isnull=True)
    c['projects'] = p
    
    return render(request, 'projects_2014_2.html', c)
