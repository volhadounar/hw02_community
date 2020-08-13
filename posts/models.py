# из модуля db импортируем класс models
from django.db import models
# из модуля auth импортируем функцию get_user_model 
from django.contrib.auth import get_user_model


User = get_user_model() 

class Group(models.Model):
    title = models.TextField()
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Post(models.Model):
    # имя_свойства = models.тип_данных()
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)


