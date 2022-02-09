# Generated by Django 3.2.6 on 2022-01-03 08:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_Name', models.CharField(max_length=1000, null=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(1000)])),
                ('category_Description', models.TextField(max_length=3000, null=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(3000)])),
                ('category_Image', models.FileField(upload_to='static/uploaded_Files')),
            ],
        ),
    ]
