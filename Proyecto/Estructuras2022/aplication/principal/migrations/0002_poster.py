# Generated by Django 4.0.2 on 2022-03-30 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=70)),
                ('price', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
            ],
        ),
    ]
