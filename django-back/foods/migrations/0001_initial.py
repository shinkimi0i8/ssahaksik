# Generated by Django 3.2.12 on 2022-06-15 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('food_img', models.ImageField(default='default.png', upload_to='food-images/')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SideDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DailyFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.date')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.food')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.region')),
                ('side_dish', models.ManyToManyField(related_name='daily_foods', to='foods.SideDish')),
            ],
        ),
    ]