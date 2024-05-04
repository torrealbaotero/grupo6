from django.urls import path
from .views import login_usuario, home, form_inventario,form_del_inventario,form_mod_inventario, form_api, form_api_back


urlpatterns = [
    path('', login_usuario, name="login_usuario"),
    path('home',home, name="home"),
    path('form-inventario',form_inventario,name="form_inventario"),
    path('form-mod-inventario/<id>',form_mod_inventario,name="form_mod_inventario"),
    path('form-del-inventario/<id>',form_del_inventario,name="form_del_inventario"),
    path('form-api', form_api,name="form_api"),
    path('form-api-back',form_api_back, name="form_api_back"),
]
