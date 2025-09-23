from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro_pessoa, name='cadastro_pessoa'),
    path('alterar/<int:id_pessoa>/', views.alterar_pessoa, name='alterar_pessoa'),
    path('deletar/<int:id_pessoa>/', views.deletar_pessoa, name='deletar_pessoa'),
]
=======
    path('', views.home, name='home'),  
    path('cadastro/', views.cadastro_pessoa, name='cadastro_pessoa'),  
]
>>>>>>> a4e35f3e5af471a8141c901b06f799f79ccedde5
