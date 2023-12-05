# Generated by Django 4.2.7 on 2023-12-05 06:55

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
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('choice_1', models.CharField(max_length=200)),
                ('choice_2', models.CharField(max_length=200)),
                ('choice_3', models.CharField(max_length=200)),
                ('choice_4', models.CharField(max_length=200)),
                ('correct_answer', models.CharField(max_length=200)),
                ('hint', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizz.category')),
            ],
        ),
    ]
