# Generated by Django 5.1.5 on 2025-02-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('publish_status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('soon', 'coming soon')], default='draft', max_length=20)),
                ('access', models.CharField(choices=[('anyone', 'Anyone'), ('email', 'Email Required')], default='email', max_length=20)),
            ],
        ),
    ]
