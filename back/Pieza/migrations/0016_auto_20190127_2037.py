# Generated by Django 2.1.4 on 2019-01-27 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pieza', '0015_auto_20190127_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultadogeneral',
            name='ejecucion',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Pieza.Ejecucion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resultadogeneral',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]