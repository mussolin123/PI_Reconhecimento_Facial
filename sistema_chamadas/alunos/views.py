from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer

# API para CRUD do Aluno
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

from django.shortcuts import render

def alunos_index(request):
    return render(request, 'alunos/index.html')

def alunos_create(request):
    return render(request, 'alunos/create.html')

def alunos_edit(request, id):
    return render(request, 'alunos/edit.html', {'id': id})
