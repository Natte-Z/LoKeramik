# Generated by Django 3.0.7 on 2021-01-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=6)),
                ('duration', models.CharField(blank=True,
                 max_length=15, null=True)),
                ('participants', models.DecimalField
                 (decimal_places=0, max_digits=1)),
                ('level', models.CharField
                 (blank=True, max_length=15, null=True)),
                ('image', models.ImageField(blank=True,
                 null=True, upload_to='')),
            ],
        ),
    ]
