from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
# Create your views here.
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
#def home(request):
#    post_list = Article.objects.all()
#    return render(request,'myhome.html',{'post_list':post_list})

def home(request):
    posts = Article.objects.all()  #获取全部的Article对象
    paginator = Paginator(posts, 4) #每页显示4个
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'myhome.html', {'post_list' : post_list})



def detail(request,my_args):
    post = Article.objects.get(id=int(my_args))
    return render(request,'mypost.html',{'post':post})
def person(request):
    post_list = Article.objects.all()
    return render(request,'index.html',{'post_list':post_list})
