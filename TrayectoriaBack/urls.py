from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
# from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views

from api import views




# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('products', views.ProductView)

urlpatterns = [
    path('admin/', admin.site.urls),
    #API_URLS
    path('api/v1/', include(router.urls)),
    #AUTH_URLS
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
]
# re_path(r'^', include(router.urls)),
# re_path(r'^api/v1/login/', include('Login.urls')),
# re_path(r'^api/v1/profile/', include('Profile.urls')),
# re_path(r'^api/v1/user/', include('User.urls')),
#path('api_generate_token/',views.obtain_auth_token),
