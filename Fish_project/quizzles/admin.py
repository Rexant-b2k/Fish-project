from django.contrib import admin

from .models import Task, Category, Hint
# Register your models here.

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Hint)
