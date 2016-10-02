"""
    Django polls application views
"""

from django.http import HttpResponse

def index(request):
    """
        index view: welcome page
    """
    return HttpResponse("Hello, world. You're at the polls index.")
