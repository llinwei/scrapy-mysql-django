from django.shortcuts import render
from django.http import HttpResponse
from .models import Qidian
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.
def index(request,index=1):
    novels = Qidian.objects.all()
    paginator = Paginator(novels, 10)
    try:
        book_list = paginator.page(index)#获取当前页码的记录
    except PageNotAnInteger:
        book_list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request,'qd/index.html',{'novels':book_list})