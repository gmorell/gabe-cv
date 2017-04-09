from django.conf import settings

def ga_tracking_id(request):
    if settings.GA_TRACKING_ID:
        return {"ga_tracking": True, "ga_tracking_id": settings.GA_TRACKING_ID}
    else:
        return {"ga_tracking": False, "ga_tracking_id": None}
