# Generated by Django 5.1.3 on 2024-11-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RelatorioEstoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_produto', models.IntegerField()),
                ('nome', models.CharField(max_length=255)),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField()),
                ('descricao', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
            ],
        ),
    ]
