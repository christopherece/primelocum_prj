# Generated by Django 5.1.5 on 2025-01-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_certification_education_skill_profile_interests_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
