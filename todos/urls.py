from django.urls import path
from todos.views import new_todo, list_todo, todo_details, edit, delete  


app_name = 'todos'

urlpatterns = [
    path('new/', new_todo, name='new'),
    path('', list_todo, name='home'),
    path('todos/<int:pk>/', todo_details, name='todo_details'),
    path('todos/<int:pk>/edit', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
]


