from django.db import models
from materias.models import Materia

class Aluno(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    ano_ingresso = models.IntegerField()
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    materias = models.ManyToManyField(Materia, related_name='alunos')

    def __str__(self):
        return self.nome
