# Generated by Django 4.2.1 on 2023-05-28 17:20

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
                ('text', models.CharField(choices=[('Math', 'Математика'), ('Fish', 'Рыбки')], max_length=128, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, verbose_name='Тест задачи')),
                ('image', models.ImageField(blank=True, upload_to='quizzles/', verbose_name='Изображение')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='quizzles.category', verbose_name='Категория задачи')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(1, 'Light'), (2, 'Medium'), (3, 'Full')], verbose_name='Уровень подсказки')),
                ('text', models.TextField(verbose_name='Подсказка')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hints', to='quizzles.task')),
            ],
        ),
        migrations.AddConstraint(
            model_name='task',
            constraint=models.CheckConstraint(check=models.Q(('text__isnull', False), ('image__isnull', False), _connector='OR'), name='Text_or_Image', violation_error_message='text or image is mandatory'),
        ),
    ]
