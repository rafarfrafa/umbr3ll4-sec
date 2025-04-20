from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('login/', views.login_View, name='Login'),
    path('admin/', views.admin_login_View, name='admin_login'),
    path('logout/', views.logout_View, name='Logout'),
    path('painel/', views.painel_admin, name='painel_admin'),
    path('editar_usuario/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('deletar_usuario/<int:user_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('login/Registro/', views.Register_View, name='Registro'),  # Certifique-se de que a URL está nomeada corretamente
]