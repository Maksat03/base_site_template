# Generated by Django 4.2.5 on 2023-09-10 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide_images/')),
                ('link', models.CharField(default='/', max_length=500)),
            ],
        ),
    ]
