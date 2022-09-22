from rest_framework import routers
from django.urls import path,include
from .views import CitasViewsets,PublicacionViewsets,RegistroUsuarioViewsets,RegistroTatuadoresViewsets

router = routers.DefaultRouter()
router.register('citas',CitasViewsets)
router.register('Publicacion',PublicacionViewsets)
router.register('RegistroTatuadores',RegistroTatuadoresViewsets)
router.register('RegistroUsuario',RegistroUsuarioViewsets)



urlpatterns = [
    path('api/',include(router.urls)),
]