# animais/urls.py

from django.urls import path
from .views import ListaReinosView, ListaFilosView, ListaSubfilosView, ListaEspeciesView

urlpatterns = [
    path('', ListaReinosView.as_view(), name='lista_reinos'),
    path('reinos/<int:id_reino>/', ListaFilosView.as_view(), name='lista_filos'),
    path('filos/<int:id_filo>/', ListaSubfilosView.as_view(), name='lista_subfilos'),
    path('subfilos/<int:id_subfilo>/', ListaEspeciesView.as_view(), name='lista_especies'),
]
