# Generated by Django 4.2.1 on 2023-06-03 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('task_date', models.DateTimeField(auto_now_add=True)),
                ('task_status', models.BooleanField()),
            ],
        ),
    ]
