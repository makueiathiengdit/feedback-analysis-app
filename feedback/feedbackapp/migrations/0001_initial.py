# Generated by Django 4.2.3 on 2023-08-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('label', models.CharField(max_length=50, null=True)),
                ('score', models.IntegerField(null=True)),
            ],
        ),
    ]
