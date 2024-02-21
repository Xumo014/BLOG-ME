# Generated by Django 5.0.1 on 2024-01-19 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('image', models.FileField(upload_to='post-images')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]