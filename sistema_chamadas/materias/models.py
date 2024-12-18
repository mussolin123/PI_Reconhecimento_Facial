from django.db import models

class Materia(models.Model):
    nome = models.CharField(max_length=255)
    dia_semana = models.CharField(max_length=20)
    professor = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
