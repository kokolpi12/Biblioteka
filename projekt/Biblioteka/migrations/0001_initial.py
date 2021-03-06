# Generated by Django 4.0.5 on 2022-06-23 11:56

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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tytuł')),
                ('author', models.CharField(max_length=200, verbose_name='Autor')),
                ('cover', models.CharField(choices=[('Twarda', 'Twarda'), ('Miękka', 'Miękka')], default='T', max_length=30, verbose_name='Okładka')),
                ('publisher', models.CharField(max_length=200, verbose_name='Wydawnictwo')),
                ('premiere_date', models.DateField(verbose_name='Data premiery')),
                ('pub_date', models.DateField(default=None, verbose_name='Data publikacji')),
                ('number_of_pages', models.IntegerField(verbose_name='Liczba stron')),
                ('photo', models.ImageField(blank=True, upload_to='images', verbose_name='Zdjęcie')),
                ('deleted', models.BooleanField(default=False, verbose_name='Usunięta? ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
