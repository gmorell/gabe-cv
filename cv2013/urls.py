from django.conf.urls import include, url
from django.contrib import admin
from django.http.response import HttpResponse
from rest_framework.routers import DefaultRouter

from api import views as views_api
from cv import views as views_c
from docs.views import DocumentDetail
from msite import views as views_m
from pages import views as views_pa
from projects import views as views_p

router = DefaultRouter()
router.register(r'pages', views_api.PageROViewSet)
router.register(r'cv', views_api.CVROViewSet)
router.register(r'projects', views_api.ProjectViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsettings.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views_m.index, name="index"),

    url(r'^cv/$',       views_c.index,          name="cv_index"),
    url(r'^cv/pdf/$',   views_c.index_as_pdf,   name="cv_pdf"),

    url(r'^contact/$', views_m.contact),

    url(r'^projects/$', views_p.project_list, name="projects"),
    url(r'^log/$', views_p.log, name="log_list"),
    url(r'^log/(\d+)/$', views_p.log, name="log_detail"),
    url(r'^log/(?P<slug>[-\w]+)/$',views_p.log_project, name="log_project"),
    url(r'^log/(?P<project>[-\w]+)/(?P<slug>[-\w]+)/$', views_p.log_perma, name="log_perma"),

    url(r'^documents/(?P<slug>[0-9a-f]+)/', DocumentDetail.as_view(), name="doc-view"),
    url(r'^_', lambda r: HttpResponse("Anything is Possible if You Believe")),
    url(r'^p/(?P<slug>[-\w]+)/$', views_pa.page, name="page-view"),
    url(r'^a/', include('allauth.urls')),
    url(r'^api', include(router.urls)),
    url(r'^api/ns$', views_api.set_nightshift_cookie, name="api-cookie-nightshift"),
    url(r'^api/nst', views_api.set_nightshift_toggle, name="api-cookie-nightshift-toggle"),
    url(r'^api/projects', views_api.set_nightshift_toggle, name="api-cookie-nightshift-toggle"),
]


#
