from django.shortcuts import render
from list import models
# Create your views here.
def index(request):
    todo_list_all = models.ToDu.objects.all()
    if todo_list_all:
        return render(request,'index.html',{'todo_list_all':todo_list_all})
    else:
        mesage = "数据库为空"
        return render(request, 'index.html', {'erro':mesage})