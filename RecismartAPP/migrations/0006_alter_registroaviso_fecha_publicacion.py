# Generated by Django 4.1.4 on 2022-12-12 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecismartAPP', '0005_fotos_alter_registroaviso_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroaviso',
            name='Fecha_publicacion',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 1, 51, 39, 281590, tzinfo=datetime.timezone.utc)),
        ),
    ]
