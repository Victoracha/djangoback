# Generated by Django 2.1.4 on 2019-01-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pieza', '0010_auto_20190124_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='piezaresultado',
            name='indiceResultado',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
