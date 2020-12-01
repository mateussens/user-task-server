from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from task.views import TaskViewSet
from user.views import UserViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, 'users')
router.register(r'tasks', TaskViewSet, 'tasks')

schema_view = get_schema_view(
    openapi.Info(
        title="User API",
        default_version='v1',
        description="API for technical testing for Smarket",
        contact=openapi.Contact(email="mateussens@gmail.com")
    ),
    public=True
)

urlpatterns = [
    url(r'^doc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api/', include(router.urls))
]

urlpatterns += staticfiles_urlpatterns()
