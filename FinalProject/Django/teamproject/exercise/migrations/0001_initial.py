# Generated by Django 4.2.1 on 2023-08-31 07:06

from django.db import migrations, models
import django_base64field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_name', models.CharField(blank=True, max_length=100)),
                ('ex_part', models.CharField(blank=True, max_length=50)),
                ('ex_method', models.TextField()),
                ('ex_video1', models.TextField()),
                ('ex_video2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ImgModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=50, null=True)),
                ('img_data', django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True)),
                ('ex_class', models.IntegerField()),
                ('ex_name', models.CharField(max_length=50)),
                ('ex_per', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
