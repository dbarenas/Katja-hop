from django.conf.urls import url, include
from rest_framework import routers
from album.views import UserViewSet, GroupViewSet, AlbumViewSet
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'track', AlbumViewSet)
 
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [

	url(r'^', include(router.urls)),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]