# Generated by Django 4.1.7 on 2023-03-11 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, default=None)),
                ('location', models.TextField(blank=True, default=None)),
                ('gmail', models.EmailField(blank=True, default=None, max_length=254)),
                ('linkedin', models.URLField(blank=True, default=None)),
                ('github', models.URLField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('affiliation', models.TextField(blank=True, default=None)),
                ('location', models.CharField(blank=True, default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=200)),
                ('description', models.TextField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SkillsDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('my_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.skills')),
            ],
        ),
        migrations.CreateModel(
            name='MyModelDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('my_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.mymodel')),
            ],
        ),
    ]