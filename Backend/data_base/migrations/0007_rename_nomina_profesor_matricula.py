# Generated by Django 4.2.1 on 2023-06-09 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_base', '0006_delete_login_profesor_nomina_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='nomina',
            new_name='matricula',
        ),
    ]
