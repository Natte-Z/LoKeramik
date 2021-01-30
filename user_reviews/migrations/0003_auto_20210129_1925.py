# Generated by Django 3.0.7 on 2021-01-29 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210126_1504'),
        ('user_reviews', '0002_auto_20210129_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreview',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='courses.Course'),
        ),
    ]