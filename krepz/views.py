from django.shortcuts import render
from krepz.map_genrator import create_map


def home(request):
    map_html = create_map()
    context = {'basic_map': map_html}
    return render(request, 'home.html', context)

