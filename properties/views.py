from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property

# cache the view for 15 minutes (900 seconds)
@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values()
    return JsonResponse({
        "data": list(properties)
    }, safe=False)
