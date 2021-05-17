# Generated by Django 3.2.3 on 2021-05-16 07:55

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=130)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=130)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=130)),
                ('thumbnail', models.ImageField(upload_to='blog/thumbnails/')),
                ('banner', models.ImageField(upload_to='blog/banners/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('seo_title', models.CharField(blank=True, max_length=120, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=200, null=True)),
                ('seo_tags', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
    ]
