# Generated by Django 4.1.7 on 2023-03-08 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cities', '0002_alter_city_country_alter_city_last_modified_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_city', to='Cities.country'),
        ),
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='continent_country', to='Cities.continent'),
        ),
    ]
