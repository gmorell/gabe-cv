class NightShiftMiddleware(object):
    def __init__(self, get_response, **kwargs):
        self.get_response = get_response
    #     # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # if the nightshift cookie is set let's use it
        # print(request.session.get('nightshiftstate'))
        if request.COOKIES.get('nightshift'):
            # if it's already in the session, we're set in the processor
            request.session['nightshiftstate'] = request.COOKIES.get('nightshift')

            print(request.COOKIES.get('nightshift'))
        else:
            pass
        # Code to be executed for each request/response after
        # the view is called.

        return response

