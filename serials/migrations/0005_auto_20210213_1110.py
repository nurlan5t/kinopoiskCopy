# Generated by Django 3.1.4 on 2021-02-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serials', '0004_auto_20210208_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='serials',
            field=models.ManyToManyField(null=True, related_name='cast', to='serials.Serial'),
        ),
    ]
