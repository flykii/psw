from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    carga_horaria = models.IntegerField(null=False)
    logo = models.ImageField(upload_to='logos')
    participantes = models.ManyToManyField(User, related_name='evento_participante', null=True, blank=True)

    #paletas de cores hexadecimais
    cor_principal = models.CharField(max_length=7)
    cor_secondaria = models.CharField(max_length=7)
    cor_fundo = models.CharField(max_length=7)

    def __str__(self):
        return self.nome
    
class Certificado(models.Model):
    certificado = models.ImageField(upload_to='certificados')
    participantes = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING)
    
