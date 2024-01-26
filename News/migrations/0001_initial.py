# Generated by Django 4.2.7 on 2024-01-09 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('resim', models.FileField(upload_to='author_images')),
                ('bilgi', models.CharField(max_length=250)),
                ('pozisyon', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=100)),
                ('resim', models.FileField(upload_to='news_images')),
                ('tarih', models.DateField()),
                ('icerik', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='News.category')),
                ('yazar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='News.author')),
            ],
        ),
    ]