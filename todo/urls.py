from django.urls import path, include
from . import views
from .router import urlpatterns as router_urls
from .views import LoginView

urlpatterns = [
    path('', include(router_urls)), 
    path('api/', include(router_urls)),
    path('login/', LoginView.as_view(), name='login'),  
]
