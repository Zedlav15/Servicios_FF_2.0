# Generated by Django 5.0.3 on 2024-03-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_servicios', '0002_remove_usuarioservicio_numero_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioservicio',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuarioservicio',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$Pe1HJG7Rp1bP6uK8i8t5q1$2jmj7l5rSw0yVb/vlWAYkK/YBwk=', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuarioservicio',
            name='contrasena',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='usuarioservicio',
            name='correo_electronico',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
