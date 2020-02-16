from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.upload_image, name = 'upload_image')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
