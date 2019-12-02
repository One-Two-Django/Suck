from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from quantum import views
app_name = 'quantum'
urlpatterns = [
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)