from django.db import models

# Create your models here.
class Parking(models.Model):
    cnpj = models.CharField("CNPJ", max_length=14, unique=True)
    nome_estacionamento = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30, default='')
    numero = models.CharField(max_length=5, verbose_name="Número")
    complemento = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default='SP',
        choices = (
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )
    horario_abertura = models.TimeField(verbose_name="Horário abertura")
    horario_fechamento = models.TimeField(verbose_name="Horário abertura")
    preco_hora = models.FloatField(verbose_name="Preço hora")
    total_vagas = models.IntegerField()

    def __str__(self):
        return self.nome_estacionamento