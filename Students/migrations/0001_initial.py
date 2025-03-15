# Generated by Django 5.1.6 on 2025-03-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('year', models.CharField(choices=[('first', 'first'), ('second', 'second'), ('third', 'third'), ('fourth', 'fourth')], default='first', max_length=6, verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': 'студенты',
                'ordering': ['last_name'],
            },
        ),
    ]
