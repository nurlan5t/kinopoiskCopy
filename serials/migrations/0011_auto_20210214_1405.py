# Generated by Django 3.1.4 on 2021-02-14 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serials', '0010_auto_20210214_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='serial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='serials.serial'),
        ),
    ]