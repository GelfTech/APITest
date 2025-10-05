from django.urls import path
from .views import UsuarioListCreate, UsuarioDetail


urlpatterns = [
    path('', UsuarioListCreate.as_view(), name='usuario-list-create'),
    path('<int:IdRegistro>/', UsuarioDetail.as_view(), name='usuario-detail'),
]