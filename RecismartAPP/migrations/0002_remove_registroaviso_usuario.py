# Generated by Django 4.1.4 on 2022-12-14 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RecismartAPP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registroaviso',
            name='usuario',
        ),
    ]