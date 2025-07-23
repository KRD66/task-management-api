from django.urls import path, include
from . import views
from .router import urlpatterns as router_urls

urlpatterns = [
    path('', views.api_root),
    path('', include(router_urls)), 
    path('api/', include(router_urls)),  
]
