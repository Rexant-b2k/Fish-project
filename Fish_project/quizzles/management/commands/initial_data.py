from django.core.management.base import BaseCommand
from quizzles.models import Task, Category, Hint

class Command(BaseCommand):

    def _create_data(self):
        cat1 = Category.objects.create(text='Math')
        cat2 = Category.objects.create(text='Fish')
        task1 = Task.objects.create(header='Площадь прямоугольного треугольника', text='Найти площадь прямоугольного треугольника с катетами 6 см и 8 см.', category=cat1, answer=24)
        task2 = Task.objects.create(header='Изменение цены', text='Сколько будут стоить сапоги после повышения цены на 10%, если исходная цена 100р', category=cat1, answer=110)
        hint1 = Hint.objects.create(task=task1, level=1, text='Треугольник - половина прямоугольника')
        hint2 = Hint.objects.create(task=task2, level=1, text='Сначала можно найти повышение - это 1/10 от изначальной цены')
        
        task3 = Task.objects.create(header='test', text='что это за рыбка?', category=cat2, answer='неизвестно')
        task4 = Task.objects.create(header='Телефонные номера', text='Какова вероятность того, что случайно выбранный телефонный номер оканчивается двумя чётными цифрами? (ответ ввести в виде десятичной дроби с помощью запятой)', category=cat1, answer=0.25)
        hint4 = Hint.objects.create(task=task4, level=1, text='Вероятность, что на каждом из двух последних мест стоит четная цифра 0,5')

        task5 = Task.objects.create(header='Площадь квадрата', text='Найдите площадь квадрата, если его диагональ равна 2.', category=cat1, answer=2)
        hint5 = Hint.objects.create(task=task5, level=1, text='Используй теорему Пифагора')

        task6 = Task.objects.create(header='Деление конфет', text=' Однажды отец дал детям 130 конфет и сказал: «Разделите их на 2 части так, чтобы меньшая часть увеличенная в 4 раза. равнялась бы большей части, уменьшенной в 3 раза». Как детям разделить конфеты? (в ответ запишите количество конфет в меньшей части).', category=cat1, answer=10)
        hint6 = Hint.objects.create(task=task6, level=1, text='Пусть в меньшей части будет x конфет, тогда в большей части 130-x конфет. Какое можно составить уравнение')

        task7 = Task.objects.create(header='Приготовление компота', text='Для приготовления компота необходимо смешать воду, сахар и яблоки в отношении 20:3:7, соответственно. Сколько потребуется килограмм сахара и яблок суммарно на 10 кг воды?', category=cat1, answer=5)
        hint7 = Hint.objects.create(task=task7, level=1, text='Обозначить количество воды в компоте 20x')
        
        task8 = Task.objects.create(header='Кто выше?', text='Гоша выше Бориса, но ниже Антона. Витя выше Димы, но ниже Гоши. Кто из мальчиков самый высокий?', category=cat1, answer='Антон')
        hint8 = Hint.objects.create(task=task8, level=1, text='Если мальчик ниже кого-то, то он не может быть самым высоким')

        task9 = Task.objects.create(header='Приготовление рыбов', image='quizzles/Jo.jpg', category=cat2, answer='Джо не делится едой!')

 
    def handle(self, *args, **options):
        self._create_data()