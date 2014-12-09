from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from .views import NotaViewSet

router = routers.SimpleRouter()
router.register(r'notas',NotaViewSet)
 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
)
