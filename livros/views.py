from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LivrosSerializer

from .models import Livro


class LivrosApiView(APIView):
    '''
    Utilize este endereço para gerenciamento de livros
    '''

    def get(self, request):
        livros = Livro.objects.all()
        serializer = LivrosSerializer(livros, many=True)
        return Response(serializer.data)

    def post(self, request):
        livro = Livro.objects.create(nome=request.data.get('nome'),
                                     autor=request.data.get('autor'),
                                     categoria=request.data.get('categoria'))
        output = {
            'nome': livro.nome,
            'autor': livro.autor,
            'categoria': livro.categoria
        }
        return Response(output)


livros_view = LivrosApiView.as_view()
