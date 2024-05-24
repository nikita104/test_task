from rest_framework import routers

from core.views.api import UserViewSet

app_name = 'core'


urlpatterns = [

]

router = routers.DefaultRouter()

router.register('api/v1/users', UserViewSet, basename='user')

urlpatterns += router.urls