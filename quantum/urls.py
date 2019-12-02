from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = 'quantum'
urlpatterns = [
  path('', views.screen_list, name='screen_list'),
  path('<int:screen_id>/', views.detail, name="detail"),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)