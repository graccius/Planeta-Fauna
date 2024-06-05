from django.views.generic import TemplateView, ListView, DetailView
from .models import Reino, Filo, Classe, Ordem, Familia, Genero, Especie
from .utils import get_class_name


class SearchView(ListView):
    template_name = 'search_results.html'
    context_object_name = 'results'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = []
        if query:
            reinos = Reino.objects.filter(nome__icontains=query)
            filos = Filo.objects.filter(nome__icontains=query)
            classes = Classe.objects.filter(nome__icontains=query)
            ordens = Classe.objects.filter(nome__icontains=query)
            especies = Especie.objects.filter(nome__icontains=query)
            
            object_list = list(reinos) + list(filos) + list(subfilos) + list(especies)
        return object_list

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reinos'] = Reino.objects.all()
        return context

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

class ListaClassesView(ListView):
    template_name = 'lista_classes.html'
    context_object_name = 'classes'

    def get_queryset(self):
        filo_id = self.kwargs['id_filo']
        return Classe.objects.filter(filo_id=filo_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filo'] = Filo.objects.get(id=self.kwargs['id_filo'])
        return context

class ListaOrdensView(ListView):
    template_name = 'lista_ordens.html'
    context_object_name = 'ordens'

    def get_queryset(self):
        classe_id = self.kwargs['id_classe']
        return Ordem.objects.filter(classe_id=classe_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classe'] = Classe.objects.get(id=self.kwargs['id_classe'])
        return context

class ListaFamiliasView(ListView):
    template_name = 'lista_familias.html'
    context_object_name = 'familias'

    def get_queryset(self):
        ordem_id = self.kwargs['id_ordem']
        return Familia.objects.filter(ordem_id=ordem_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordem'] = Ordem.objects.get(id=self.kwargs['id_ordem'])
        return context

class ListaGenerosView(ListView):
    template_name = 'lista_generos.html'
    context_object_name = 'generos'

    def get_queryset(self):
        familia_id = self.kwargs['id_familia']
        return Genero.objects.filter(familia_id=familia_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['familia'] = Familia.objects.get(id=self.kwargs['id_familia'])
        return context

class ListaEspeciesView(ListView):
    template_name = 'lista_especies.html'
    context_object_name = 'especies'

    def get_queryset(self):
        genero_id = self.kwargs['id_genero']
        return Especie.objects.filter(genero_id=genero_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genero'] = Genero.objects.get(id=self.kwargs['id_genero'])
        return context