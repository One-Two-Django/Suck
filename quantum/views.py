from django.shortcuts import render, get_object_or_404
from .models import Screen,Pic
from django.utils import timezone
import json
from django.core import serializers
# Create your views here.

def screen_list(request):
    
    screens = Screen.objects.order_by('created_date')
    return render(request, 'quantum/screen_list.html', {'screens': screens})
def detail(request, screen_id):
    screen = get_object_or_404(Screen, pk=screen_id)
    pics = Pic.objects.filter(screen = screen)
    pic_json = serializers.serialize("json",pics)
    
    return render(request, 'quantum/detail.html', {'screen': screen ,'pic_list': pic_json})
    
