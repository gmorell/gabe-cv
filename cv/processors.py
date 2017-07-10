from django.conf import settings

def ga_tracking_id(request):
    if settings.GA_TRACKING_ID:
        return {"ga_tracking": True, "ga_tracking_id": settings.GA_TRACKING_ID}
    else:
        return {"ga_tracking": False, "ga_tracking_id": None}

def nightshift_tmpl(request):
    return {"nightshift_enabled": request.session.get('nightshiftstate', False)}

def anchorware_tmpl(request):
    if request.session.get('anchorware', "False") == "True":
        print(type(request.session.get('anchorware', 'XXX')))
        return {"ancw": "#cb"}
    print("FFF")
    return {"ancw":""}
