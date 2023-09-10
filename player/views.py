from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.cache import cache_control

from . models import TRACK_LINKS

def index(request):
    context = {"tracks": TRACK_LINKS.keys()}
    return render(request, 'index.html', context)

# @cache_control(max_age=3600)
def player(request: HttpRequest):
    track_name = request.GET.get('track')
    track_link = TRACK_LINKS.get(track_name)
    context = {"track_name": track_name, "track_link": track_link}
    return render(request, 'player.html', context)