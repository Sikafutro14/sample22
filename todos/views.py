from django.shortcuts import render
from todos.models import Todo
from django.http import HttpResponse

# Create your views here.
def index(request):
    todo = Todo.objects.all()
    return HttpResponse(todo)