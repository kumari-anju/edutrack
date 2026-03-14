from django.utils.cache import add_never_cache_headers

class NoCacheAuthenticatedMiddleware:
    """
    Middleware to ensure that authenticated pages are not cached by the browser.
    This prevents users from hitting the back button after logging out and seeing
    sensitive or authenticated-only information.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # If the user is authenticated, we add cache-control headers
        # to prevent the browser from caching the page.
        if hasattr(request, 'user') and request.user.is_authenticated:
            add_never_cache_headers(response)
            
        return response
