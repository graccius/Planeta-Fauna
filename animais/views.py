from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, TemplateView, ListView
from .models import Reino, Filo, Classe, Ordem, Familia, Genero, Especie


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reinos'] = Reino.objects.all()  # Adicione esta linha para passar os reinos para o template
        return context


class SearchView(ListView):
    template_name = 'search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # Buscar em todos os modelos relevantes
            reinos = Reino.objects.filter(nome__icontains=query)
            filos = Filo.objects.filter(nome__icontains=query)
            classes = Classe.objects.filter(nome__icontains=query)
            ordens = Ordem.objects.filter(nome__icontains=query)
            familias = Familia.objects.filter(nome__icontains=query)
            generos = Genero.objects.filter(nome__icontains=query)
            especies = Especie.objects.filter(nome__icontains=query)

            # Agregar todos os resultados em uma lista
            results = list(reinos) + list(filos) + list(classes) + \
                      list(ordens) + list(familias) + list(generos) + \
                      list(especies)

            return results

        # Retorna uma lista vazia se não houver consulta
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


## List Views ##
class ListaFilosView(View):
    def get(self, request, id_reino):
        reino = get_object_or_404(Reino, id=id_reino)
        filos = Filo.objects.filter(reino=reino)
        context = {
            'reino': reino,
            'filos': filos
        }
        return render(request, 'lista_filos.html', context)

class ListaClassesView(View):
    def get(self, request, id_filo):
        filo = get_object_or_404(Filo, id=id_filo)
        classes = Classe.objects.filter(filo=filo)
        context = {
            'filo': filo,
            'classes': classes
        }
        return render(request, 'lista_classes.html', context)

class ListaOrdensView(View):
    def get(self, request, id_classe):
        classe = get_object_or_404(Classe, id=id_classe)
        ordens = Ordem.objects.filter(classe=classe)
        context = {
            'classe': classe,
            'ordens': ordens
        }
        return render(request, 'lista_ordens.html', context)

class ListaFamiliasView(View):
    def get(self, request, id_ordem):
        ordem = get_object_or_404(Ordem, id=id_ordem)
        familias = Familia.objects.filter(ordem=ordem)
        context = {
            'ordem': ordem,
            'familias': familias
        }
        return render(request, 'lista_familias.html', context)

class ListaGenerosView(View):
    def get(self, request, id_familia):
        familia = get_object_or_404(Familia, id=id_familia)
        generos = Genero.objects.filter(familia=familia)
        context = {
            'familia': familia,
            'generos': generos
        }
        return render(request, 'lista_generos.html', context)

class ListaEspeciesView(View):
    def get(self, request, id_genero):
        genero = get_object_or_404(Genero, id=id_genero)
        especies = Especie.objects.filter(genero=genero)
        context = {
            'genero': genero,
            'especies': especies
        }
        return render(request, 'lista_especies.html', context)


## DETAIL VIEW FOR ESPECIES ## 
class DetalhesEspecieView(DetailView):
    model = Especie
    template_name = 'detalhes_especies.html'
    context_object_name = 'especies'