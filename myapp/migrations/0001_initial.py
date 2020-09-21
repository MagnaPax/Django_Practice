# Generated by Django 3.1.1 on 2020-09-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField()),
                ('author', models.TextField()),
            ],
        ),
    ]