# Generated by Django 3.1.4 on 2020-12-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
            ],
        ),
    ]