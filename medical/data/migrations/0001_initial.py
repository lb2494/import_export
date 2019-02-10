# Generated by Django 2.1 on 2019-02-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=260)),
                ('Causes', models.TextField()),
                ('Symptoms', models.TextField()),
                ('Diagnoses', models.TextField()),
                ('treatment', models.TextField()),
            ],
        ),
    ]