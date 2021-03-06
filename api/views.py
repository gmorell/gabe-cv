# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import PageSerializer, CVSerializer, ProjectSerializer, EntrySerializer
from cv.models import Section
from pages.models import Page
from projects.models import Project, Entry
from .serializers import NightShiftSerializer

@api_view(['POST'])
def set_nightshift_cookie(request):
    """
    This endpoint is used to set the nightshift cookie
    {"enabled":"True|False"} 
    
    """
    # response = self.get_response(request)
    response = Response()
    serialized = NightShiftSerializer(data=request.data)
    if serialized.is_valid(raise_exception=True):
        response.set_cookie('nightshift', serialized.validated_data.get('enabled'))
        request.session['nightshiftstate'] = serialized.validated_data.get('enabled')
        response.data = {"nightshift": serialized.validated_data.get('enabled')}
        return response

@api_view(['GET'])
def set_nightshift_toggle(request):
    response = Response()
    if request.COOKIES.get('nightshift') == "True":
        response.set_cookie('nightshift', False)
        request.session['nightshiftstate'] = False
        response.data = {"nightshift": False}
    else:
        response.set_cookie('nightshift', True)
        request.session['nightshiftstate'] = True
        response.data = {"nightshift": True}

    return response

@api_view(['GET'])
def set_anchorware_toggle(request):
    response = Response()
    if request.COOKIES.get('anchorware') == "True":
        response.set_cookie('anchorware', False)
        request.session['anchorware'] = False
        response.data = {"anchorware": False}
    else:
        response.set_cookie('anchorware', True)
        request.session['anchorware'] = True
        response.data = {"anchorware": True}

    return response


# Pages
class PageROViewSet(ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


# CV
class CVROViewSet(ReadOnlyModelViewSet):
    queryset = Section.objects.all()
    serializer_class = CVSerializer


# projects
class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class LogEntriesViewSet(ReadOnlyModelViewSet):
    queryset = Entry.objects.filter(posted__lte=datetime.datetime.now())
    serializer_class = EntrySerializer
