from django.conf import settings

def ga_tracking_id(request):
    if settings.GA_TRACKING_ID:
        return {"ga_tracking": True, "ga_tracking_id": settings.GA_TRACKING_ID}
    else:
        return {"ga_tracking": False, "ga_tracking_id": None}

def nightshift_tmpl(request):
    print(request.session.get('nightshiftstate'))
    return {"nightshift_enabled": request.session.get('nightshiftstate', False)}
