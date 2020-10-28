# Generated by Django 3.1.2 on 2020-10-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reliefcamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('cityname', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('people', models.IntegerField()),
            ],
        ),
    ]