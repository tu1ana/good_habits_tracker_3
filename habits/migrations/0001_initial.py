# Generated by Django 4.2.8 on 2023-12-05 08:28

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
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место привычки')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Время привычки')),
                ('action', models.CharField(max_length=255, verbose_name='Действие')),
                ('is_nice', models.BooleanField(default=True, verbose_name='Приятная привычка')),
                ('frequency', models.CharField(blank=True, choices=[('ONE', 'Раз в день'), ('TWO', 'Раз в два дня'), ('THREE', 'Раз в три дня'), ('FOUR', 'Раз в четыре дня'), ('FIVE', 'Раз в пять дней'), ('SIX', 'Раз в шесть дней'), ('SEVEN', 'Раз в семь дней')], default='ONE', max_length=5, null=True)),
                ('reward', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вознаграждение')),
                ('duration', models.PositiveIntegerField(blank=True, null=True, verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='Публичная')),
                ('human', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
