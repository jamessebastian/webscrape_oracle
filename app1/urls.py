from django.urls import include, re_path
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^patch$',views.patchesApi),
    re_path(r'^$',views.disp),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)