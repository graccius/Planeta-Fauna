from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HomePageView,
    SearchView,
    ListaClassesView,
    ListaFilosView,
    ListaOrdensView,
    ListaFamiliasView,
    ListaGenerosView,
    ListaEspeciesView,
    DetalhesEspecieView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search_results'),
    path('filos/<int:id_reino>/', ListaFilosView.as_view(), name='lista_filos'),  # Novo path
    path('classes/<int:id_filo>/', ListaClassesView.as_view(), name='lista_classes'),
    path('ordens/<int:id_classe>/', ListaOrdensView.as_view(), name='lista_ordens'),  # Novo path
    path('familias/<int:id_ordem>/', ListaFamiliasView.as_view(), name='lista_familias'),  # Novo path
    path('generos/<int:id_familia>/', ListaGenerosView.as_view(), name='lista_generos'),  # Novo path
    path('especies/<int:id_genero>/', ListaEspeciesView.as_view(), name='lista_especies'),
    path('details/<int:pk>/', DetalhesEspecieView.as_view(), name='detalhes_especies')
]
