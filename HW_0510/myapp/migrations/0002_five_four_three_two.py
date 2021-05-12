# Generated by Django 3.2 on 2021-05-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Five',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Four',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('height', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5)),
                ('writer', models.CharField(max_length=5)),
                ('pub_date', models.DateField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
