# Generated by Django 5.0.4 on 2024-04-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
