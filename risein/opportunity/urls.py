from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vagas/nova/', views.criar_vaga, name='criar_vaga'),
    path('vagas/<int:id>/', views.vaga_detail, name='detalhe_vaga'),
    path('editar/<int:pk>/', views.editar_vaga, name='editar_vaga'),
    path('excluir/<int:pk>/', views.excluir_vaga, name='excluir_vaga')
]