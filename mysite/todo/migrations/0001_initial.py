# Generated by Django 4.2.3 on 2023-07-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='授業名')),
                ('description', models.TextField(blank=True, verbose_name='提出物')),
                ('deadline', models.DateField(verbose_name='締め切り')),
            ],
        ),
    ]
