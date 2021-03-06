# Generated by Django 4.0.1 on 2022-01-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14, unique=True, verbose_name='CNPJ')),
                ('nome_estacionamento', models.CharField(max_length=100, verbose_name='Nome Estacionamento')),
                ('logradouro', models.CharField(max_length=50, verbose_name='Logradouro')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('numero', models.CharField(max_length=5, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=30, verbose_name='Complemento')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2, verbose_name='Estado')),
                ('horario_abertura', models.TimeField(verbose_name='Horário Abertura')),
                ('horario_fechamento', models.TimeField(verbose_name='Horário Fechamento')),
                ('preco_hora', models.FloatField(verbose_name='Preço Hora')),
                ('total_vagas', models.IntegerField(verbose_name='Total Vagas')),
                ('registro_dados', models.DateTimeField(auto_now_add=True, verbose_name='Registro Dados')),
                ('atualizacao_dados', models.DateTimeField(auto_now=True, verbose_name='Atualização Dados')),
            ],
        ),
    ]
