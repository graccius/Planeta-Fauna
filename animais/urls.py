from django.urls import path
from .views import (
    ListaReinosView,
    ListaFilosView,
    ListaClassesView,
    ListaOrdensView,
    ListaFamiliasView,
    ListaGenerosView,
    ListaEspeciesView,
    SearchView
)

urlpatterns = [
    path('', ListaReinosView.as_view(), name='home'),
    path('reinos/', ListaReinosView.as_view(), name='lista_reinos'),
    path('reinos/<int:id_reino>/filos/', ListaFilosView.as_view(), name='lista_filos'),
    path('filos/<int:id_filo>/classes/', ListaClassesView.as_view(), name='lista_classes'),
    path('classes/<int:id_classe>/ordens/', ListaOrdensView.as_view(), name='lista_ordens'),
    path('ordens/<int:id_ordem>/familias/', ListaFamiliasView.as_view(), name='lista_familias'),
    path('familias/<int:id_familia>/generos/', ListaGenerosView.as_view(), name='lista_generos'),
    path('generos/<int:id_genero>/especies/', ListaEspeciesView.as_view(), name='lista_especies'),
    path('search/', SearchView.as_view(), name='search_results')
]
