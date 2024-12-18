from django.db import models
from alunos.models import Aluno
from materias.models import Materia

class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='presencas')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='presencas')
    data = models.DateField()
    presente = models.BooleanField()

    def __str__(self):
        return f"{self.aluno} - {self.materia} - {self.data}"
