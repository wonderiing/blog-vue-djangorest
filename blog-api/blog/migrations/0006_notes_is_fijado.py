# Generated by Django 5.0.7 on 2024-07-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='is_fijado',
            field=models.BooleanField(default=False),
        ),
    ]
