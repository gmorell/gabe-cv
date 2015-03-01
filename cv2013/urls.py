from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import TemplateView

admin.autodiscover()

from docs.views import DocumentDetail


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cv2013.views.home', name='home'),
    # url(r'^cv2013/', include('cv2013.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
        
    url(r'^$', 'msite.views.index'),
    url(r'^2014/', 'msite.views.index_2014'),
    url(r'^cv/$', 'cv.views.index'),
    url(r'^cv/2014/$', 'cv.views.index_2014'),
    url(r'^cv/pdf/$', 'cv.views.index_as_pdf'),
    url(r'^contact/$', 'msite.views.contact'),
    url(r'^contact/2014/$', 'msite.views.contact_2014'),
    url(r'^projects/$', 'projects.views.project_list'),
    url(r'^projects/2014/$', 'projects.views.project_list_2014'),
    url(r'^log/$', 'projects.views.log'),
    url(r'^log_2014/$', 'projects.views.log_2014'),
    url(r'^log/(\d+)/$', 'projects.views.log'),
    url(r'^log/(?P<slug>[-\w]+)/$', 'projects.views.log_project'),
    url(r'^log/2014/(?P<slug>[-\w]+)/$', 'projects.views.log_project', kwargs={"v2014":True}),
    url(r'^log/(?P<project>[-\w]+)/(?P<slug>[-\w]+)/$', 'projects.views.log_perma'),
    url(r'^log/2014/(?P<project>[-\w]+)/(?P<slug>[-\w]+)/$', 'projects.views.log_perma', kwargs={"v2014":True}),
    url(r'^documents/(?P<slug>[0-9a-f]+)/',DocumentDetail.as_view(),name = "doc-view"),
    url(r'^_', lambda r: HttpResponse("Anything is Possible if You Believe")),
    url(r'^-', TemplateView.as_view(template_name="base_2014_2.html")),
    (r'^a/', include('allauth.urls')),
)
