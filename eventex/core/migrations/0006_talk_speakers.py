# Generated by Django 4.1 on 2022-09-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_talk'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(to='core.speaker'),
        ),
    ]