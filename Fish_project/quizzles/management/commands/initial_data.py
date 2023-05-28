from django.core.management.base import BaseCommand
from quizzles.models import Task, Category, Hint

class Command(BaseCommand):

    def _create_data(self):
        cat1 = Category.objects.create(text='Math')
        task1 = Task.objects.create(header='Площадь прямоугольного треугольника', text='Найти площадь прямоугольного треугольника с катетами 6 см и 8 см.', category=cat1, answer=24)
        task2 = Task.objects.create(header='Изменение цены', text='Сколько будут стоить сапоги после повышения цены на 10%, если исходная цена 100р', category=cat1, answer=110)
        hint1 = Hint.objects.create(task=task1, level=1, text='Треугольник - половина прямоугольника')
        hint2 = Hint.objects.create(task=task2, level=1, text='Сначала можно найти повышение - это 1/10 от изначальной цены')
        cat2 = Category.objects.create(text='Fish')
        task3 = Task.objects.create(header='test', text='что это за рыбка?', category=cat2, answer='неизвестно')
 
    def handle(self, *args, **options):
        self._create_data()