from django.views.generic import ListView, DetailView
from .models import Reino, Filo, Subfilo, Especie

class ListaReinosView(ListView):
    model = Reino
    template_name = 'lista_reinos.html'
    context_object_name = 'reinos'

class ListaFilosView(ListView):
    template_name = 'lista_filos.html'
    context_object_name = 'filos'

    def get_queryset(self):
        reino_id = self.kwargs['id_reino']
        return Filo.objects.filter(reino_id=reino_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reino'] = Reino.objects.get(id=self.kwargs['id_reino'])
        return context

class ListaSubfilosView(ListView):
    template_name = 'lista_subfilos.html'
    context_object_name = 'subfilos'

    def get_queryset(self):
        filo_id = self.kwargs['id_filo']
        return Subfilo.objects.filter(filo_id=filo_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filo'] = Filo.objects.get(id=self.kwargs['id_filo'])
        return context

class ListaEspeciesView(ListView):
    template_name = 'lista_especies.html'
    context_object_name = 'especies'

    def get_queryset(self):
        subfilo_id = self.kwargs['id_subfilo']
        return Especie.objects.filter(subfilo_id=subfilo_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subfilo'] = Subfilo.objects.get(id=self.kwargs['id_subfilo'])
        return context
