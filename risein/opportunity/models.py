from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='empresas/', blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    TIPO_CHOICES = [
        ('aprendiz', 'Jovem Aprendiz'),
        ('estagio', 'Estágio'),
    ]

    titulo = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=100)
    remoto = models.BooleanField(default=False)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
