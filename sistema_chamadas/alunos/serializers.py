from rest_framework import serializers
from .models import Aluno, Materia

class AlunoSerializer(serializers.ModelSerializer):
    
    materias = serializers.PrimaryKeyRelatedField(
        queryset=Materia.objects.all(), many=True
    )

    class Meta:
        model = Aluno
        fields = ['id', 'matricula', 'ano_ingresso','nome', 'materias']
