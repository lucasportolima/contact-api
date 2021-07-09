# Generated by Django 2.2.24 on 2021-07-08 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('varejao', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='varejaocontact',
            options={'get_latest_by': ['pk'],
                     'managed': True, 'ordering': ['nome']},
        ),
        migrations.AlterUniqueTogether(
            name='varejaocontact',
            unique_together={('nome', 'celular')},
        ),
    ]