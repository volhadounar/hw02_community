from django.contrib import admin

# Register your models here.
from .models import Post, Group

# Модели не добавляются в интерфейс админки автоматически, ведь не все они нужны администратору. 
# Но в интерфейсе админки видны только две модели: Groups и Users. Остальные модели — служебные. Они не требуют внимания администратора и потому исключены из интерфейса. 
# Чтобы добавить модель Post в интерфейс администратора, её надо зарегистрировать в файле posts/admin.py.

class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("text", "pub_date", "author") 
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",) 
    # добавляем возможность фильтрации по дате
    list_filter = ("pub_date",) 

# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Post, PostAdmin)

class GroupAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("title", "slug", "description") 
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("title",) 
    # добавляем возможность фильтрации по дате
    list_filter = ("slug",)

admin.site.register(Group, GroupAdmin)