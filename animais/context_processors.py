# context_processors.py

from .models import Reino

def reinos_context(request):
    return {
        'reinos': Reino.objects.all()
    }
