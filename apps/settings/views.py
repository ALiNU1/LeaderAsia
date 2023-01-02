from django.shortcuts import render
from .models import Setting
from apps.news.models import News
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    news = News.objects.all()
    context = {
        'setting' : setting,
        'news' : news,
    }
    return render(request, 'news/index.html',context)