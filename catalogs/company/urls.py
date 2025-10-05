from django.urls import path
from .views import EmpresaListCreate, EmpresaDetail


urlpatterns = [
    path('', EmpresaListCreate.as_view(), name='empresa-list-create'),
    path('<int:IdEmpresa>/', EmpresaDetail.as_view(), name='empresa-detail'),
]