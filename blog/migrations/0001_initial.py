# Generated by Django 3.0.8 on 2020-07-30 12:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=50)),
                ('content', models.TextField()),
                ('author', models.CharField(default='', max_length=30)),
                ('slug', models.CharField(default='', max_length=150)),
                ('tag', models.CharField(default='', max_length=15)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]