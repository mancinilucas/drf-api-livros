import json
from django.http import HttpResponse

from .models import Livro
# Create your views here.


def livros_view(request):
    livros = Livro.objects.all()
    output = [{
        'nome': livro.nome,
        'autor': livro.autor,
        'categoria': livro.categoria
    } for livro in livros]
    return HttpResponse(json.dumps(output))
