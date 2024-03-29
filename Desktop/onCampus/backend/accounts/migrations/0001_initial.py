# Generated by Django 4.1.5 on 2023-01-24 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_landlord', models.BooleanField(default=False)),
                ('plan', models.CharField(blank=True, default='free', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('monday', models.CharField(blank=True, max_length=200)),
                ('tuesday', models.CharField(blank=True, max_length=200)),
                ('wednesday', models.CharField(blank=True, max_length=200)),
                ('thursday', models.CharField(blank=True, max_length=200)),
                ('friday', models.CharField(blank=True, max_length=200)),
                ('saturday', models.CharField(blank=True, max_length=200)),
                ('sunday', models.CharField(blank=True, max_length=200)),
                ('want_location', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
