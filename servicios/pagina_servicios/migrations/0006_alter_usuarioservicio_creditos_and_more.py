# Generated by Django 5.0.3 on 2024-03-26 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_servicios', '0005_metodopago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioservicio',
            name='creditos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usuarioservicio',
            name='rol',
            field=models.IntegerField(default=2),
        ),
    ]
