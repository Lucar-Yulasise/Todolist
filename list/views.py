from django.shortcuts import render , redirect, reverse
from Todolist import views
from .models import ToDu
# Create your views here.
def create(request):
    if request.method  == "GET":
        return render(request, 'list\creart.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status')
        todo = ToDu.objects.create()
        todo.title = title
        todo.content = content
        todo.status = status
        todo.save()
        return redirect(reverse(views.index))

def delete(request):
    if request.method == "GET":
        id = request.GET.get('id')
        ToDu.objects.filter(id=id).delete()
    return redirect(reverse(views.index))

def tolist(request):
    if request.method == "GET":
        status = request.GET.get("status")
        todo_list_all = ToDu.objects.filter(status=status)
        if todo_list_all:
            return render(request, 'list/tolist.html', {'todo_list_all': todo_list_all})