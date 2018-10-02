from django.shortcuts import render
from django.http import HttpResponse
from .models import Qidian
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.
def index(request,index=1):
    novels = Qidian.objects.all()
    paginator = Paginator(novels, 10)
    try:
        book_list = paginator.page(index)#��ȡ��ǰҳ��ļ�¼
    except PageNotAnInteger:
        book_list = paginator.page(1)#����û������ҳ�벻������ʱ,��ʾ��1ҳ������
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)#����û������ҳ������ϵͳ��ҳ���б���ʱ,��ʾ���һҳ������
    return render(request,'qd/index.html',{'novels':book_list})