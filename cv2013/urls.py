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
    
    url(r'^cv/$', 'cv.views.index'),
    url(r'^cv/pdf/$', 'cv.views.index_as_pdf'),
    
    url(r'^contact/$', 'msite.views.contact'),
   
    url(r'^projects/$', 'projects.views.project_list'),
    url(r'^log/$', 'projects.views.log'),
    url(r'^log/(\d+)/$', 'projects.views.log'),
    url(r'^log/(?P<slug>[-\w]+)/$', 'projects.views.log_project'),
    url(r'^log/(?P<project>[-\w]+)/(?P<slug>[-\w]+)/$', 'projects.views.log_perma'),
    
    url(r'^documents/(?P<slug>[0-9a-f]+)/',DocumentDetail.as_view(),name = "doc-view"),
    url(r'^_', lambda r: HttpResponse("Anything is Possible if You Believe")),
    url(r'^p/(?P<slug>[-\w]+)/$', 'pages.views.page', name="page-view"),
    (r'^a/', include('allauth.urls')),
)
