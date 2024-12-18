# Importando a parte API do Django Rest Framework
from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer

# API para CRUD do Aluno
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

# Importando a parte do Django tradicional para renderizar HTML
from django.shortcuts import render

# View para mostrar a lista de alunos (frontend HTML)
def alunos_index(request):
    return render(request, 'alunos/index.html')

# View para criar um novo aluno (frontend HTML)
def alunos_create(request):
    return render(request, 'alunos/create.html')

# View para editar um aluno específico (frontend HTML)
def alunos_edit(request, id):
    return render(request, 'alunos/edit.html', {'id': id})
