# Generated by Django 4.2.5 on 2023-10-09 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dog', '0002_alter_dogs_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/')),
                ('bio', models.TextField()),
            ],
        ),
    ]
