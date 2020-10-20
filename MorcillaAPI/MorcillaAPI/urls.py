from django.urls import include, path
from rest_framework import routers
from app import views
from django.contrib import admin
from django.conf import settings  # new
from django.conf.urls.static import static  # new

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'ciudades', views.CiudadViewSet)
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'telefonos', views.TelefonoViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
