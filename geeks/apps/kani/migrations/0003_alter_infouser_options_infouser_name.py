# Generated by Django 5.0.3 on 2024-03-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kani', '0002_rename_geeks_infouser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infouser',
            options={'verbose_name': 'Данные пользователя'},
        ),
        migrations.AddField(
            model_name='infouser',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
