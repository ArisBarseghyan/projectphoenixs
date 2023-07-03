from django.shortcuts import render, get_object_or_404
from .models import News


def news_view(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'all_news': news})


def news_detail(request, pk):
    news_obj = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news_obj})
