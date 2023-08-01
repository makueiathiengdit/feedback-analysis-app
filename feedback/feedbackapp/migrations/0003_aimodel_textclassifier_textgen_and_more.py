# Generated by Django 4.2.3 on 2023-08-01 18:40

from django.db import migrations, models
import feedbackapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0002_alter_feedback_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='AIModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.CharField(default=feedbackapp.models.generate_id, max_length=12)),
                ('model_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('1', 'AVAILABLE'), ('0', 'UNAVAILABLE')], max_length=1)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_used_date', models.DateTimeField(auto_now_add=True)),
                ('use_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TextClassifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('category', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextGen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.TextField()),
                ('time_created', models.DateField(auto_now_add=True)),
                ('generated_text', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-time_created', 'time_created'],
            },
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ('-time_created', 'time_created')},
        ),
    ]