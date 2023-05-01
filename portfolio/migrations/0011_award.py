# Generated by Django 4.1.7 on 2023-03-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_footer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('org', models.TextField()),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
