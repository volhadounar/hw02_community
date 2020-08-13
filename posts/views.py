from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . models import Post, Group


def index(request):
    # одна строка вместо тысячи слов на SQL
    latest = Post.objects.order_by('-pub_date')[:10]
    # собираем тексты постов в один, разделяя новой строкой
    output = []
    for item in latest:
        output.append(item.text)
    return HttpResponse('\n'.join(output))

def group_posts(request, slug):
    # функция get_object_or_404 получает по заданным критериям объект из базы данных 
    # или возвращает сообщение об ошибке, если объект не найден
    print(f'Tenemos {slug} ')
    try:
        group = get_object_or_404(Group, slug=slug)
    except Http404:
        print(f'{slug} not found')
        pass
    # Метод .filter позволяет ограничить поиск по критериям. Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
