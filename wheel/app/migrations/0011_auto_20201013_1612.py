# Generated by Django 3.1 on 2020-10-13 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_prize_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='draw',
            name='prizeId',
        ),
        migrations.AddField(
            model_name='draw',
            name='prize',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.prize'),
            preserve_default=False,
        ),
    ]
