from django.db import models

var_choices = (
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

# Create your models here.
class Parking(models.Model):
    cnpj = models.CharField(verbose_name="CNPJ", max_length=14, unique=True)
    nome_estacionamento = models.CharField(verbose_name="Nome Estacionamento",  max_length=100)
    logradouro = models.CharField(verbose_name="Logradouro", max_length=50)
    bairro = models.CharField(verbose_name="Bairro", max_length=30)
    numero = models.CharField(verbose_name="Número",  max_length=5)
    complemento = models.CharField(verbose_name="Complemento", max_length=30, blank=True)
    cidade = models.CharField(verbose_name="Cidade", max_length=30)
    estado = models.CharField(verbose_name="Estado", max_length=2, default='SP', choices=var_choices)
    horario_abertura = models.TimeField(verbose_name="Horário Abertura")
    horario_fechamento = models.TimeField(verbose_name="Horário Fechamento")
    preco_hora = models.FloatField(verbose_name="Preço Hora")
    total_vagas = models.IntegerField(verbose_name="Total Vagas")
    registro_dados = models.DateTimeField(verbose_name="Registro Dados", auto_now_add=True)
    atualizacao_dados = models.DateTimeField(verbose_name="Atualização Dados", auto_now=True)

    def __str__(self):
        return self.nome_estacionamento

    