from django.urls import path
from .views import discos_all,discos_detail

urlpatterns = [
    #path('api/listar_discos/', DiscosAllViewset.as_view()),
    path('api/discos/', discos_all),
    path('api/discos/<pk>', discos_detail),
]