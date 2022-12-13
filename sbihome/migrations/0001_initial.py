# Generated by Django 4.1.4 on 2022-12-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=100)),
                ('member_cellphone', models.CharField(max_length=20)),
                ('member_email', models.EmailField(max_length=254)),
                ('regdate', models.DateTimeField()),
            ],
        ),
    ]