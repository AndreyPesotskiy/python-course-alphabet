from django.urls import reverse
from django.shortcuts import redirect


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        path = request.path_info
        article_create_path = reverse('create')
        if not request.user.is_authenticated and path == article_create_path:
            return redirect(reverse('login'))

        # Code to be executed for each request/response after
        # the view is called.

        return response