# Generated by Django 2.0.5 on 2018-10-13 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0007_auto_20181012_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Choice'),
        ),
    ]