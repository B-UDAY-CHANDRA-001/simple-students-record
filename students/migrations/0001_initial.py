# Generated by Django 3.0.1 on 2020-10-31 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNo', models.IntegerField()),
                ('Name', models.CharField(max_length=20)),
                ('Branch', models.CharField(max_length=10)),
                ('mark_1', models.IntegerField()),
                ('mark_2', models.IntegerField()),
            ],
        ),
    ]
