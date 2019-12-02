from django.shortcuts import render, get_object_or_404
from .models import Screen,Pic
from django.utils import timezone
# Create your views here.

def screen_list(request):
    screens = Screen.objects.order_by('created_date')
    return render(request, 'quantum/screen_list.html', {'screens': screens})
def detail(request, screen_id):
    screen = get_object_or_404(Screen, pk=screen_id)
    return render(request, 'quantum/detail.html', {'screen': screen})
