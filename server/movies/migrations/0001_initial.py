# Generated by Django 3.2.9 on 2021-11-24 15:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('release_date', models.DateField()),
                ('backdrop_path', models.TextField(null=True)),
                ('popularity', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('poster_path', models.TextField(null=True)),
                ('vote_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('vote_average', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('adult', models.BooleanField()),
                ('original_title', models.CharField(max_length=100)),
                ('tmdb_id', models.IntegerField()),
                ('overview', models.TextField()),
                ('genres', models.ManyToManyField(related_name='genre_movies', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('popularity', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('profile_path', models.TextField(null=True)),
                ('adult', models.BooleanField()),
                ('gender', models.IntegerField()),
                ('tmdb_id', models.IntegerField()),
                ('also_known_as', models.JSONField(null=True)),
                ('known_for_department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MovieSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=200)),
                ('link', models.CharField(blank=True, max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=200, validators=[django.core.validators.MinLengthValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='people',
            field=models.ManyToManyField(related_name='people_movies', to='movies.People'),
        ),
        migrations.AddField(
            model_name='movie',
            name='want',
            field=models.ManyToManyField(blank=True, related_name='user_wants', to=settings.AUTH_USER_MODEL),
        ),
    ]
