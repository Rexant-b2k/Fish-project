from django.contrib.auth import get_user_model
from django.db import models

CATEGORY = (
    ('Math', 'Математика'),
    ('Fish', 'Рыбки'),
)

LEVELS = (
    (1, 'Light'),
    (2, 'Medium'),
    (3, 'Full')
)

User = get_user_model()

class Category(models.Model):
    text = models.CharField(
        'Категория',
        max_length=128,
        choices=CATEGORY,
        unique=True
    )

    def __str__(self) -> str:
        return self.text


class Task(models.Model):
    header = models.CharField('Заголовок', max_length=64)
    text = models.TextField('Тест задачи', blank=True)
    image = models.ImageField(
        'Изображение',
        upload_to='quizzles/',
        blank=True
    )
    add_date = models.DateTimeField('Дата добавления',
                                    auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Категория задачи'
    )
    answer = models.CharField('Ответ', max_length=300)
    topic = models.CharField('Тема задачи', max_length=100, default='Общая тема')
    
    def __str__(self) -> str:
        return self.header

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        constraints = [
            models.CheckConstraint( # должно работать
                check=models.Q(text__isnull=False) | models.Q(image__isnull=False),
                name='Text_or_Image',
                violation_error_message='text or image is mandatory'
            )
        ]


class Hint(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='hints'
    )
    level = models.IntegerField('Уровень подсказки', choices=LEVELS)
    text = models.TextField('Подсказка')
