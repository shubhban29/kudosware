from django.urls import path
from .views import ToDoView, UserToDoView
todo_getall = UserToDoView.as_view({'get': 'getall'})
todo_get = UserToDoView.as_view({'get': 'retrieve'})
todo_put = ToDoView.as_view({'put': 'put'})
todo_delete = ToDoView.as_view({'delete': 'delete'})
todo_create = ToDoView.as_view({'post': 'create'})
urlpatterns = [
    path('getall',todo_getall),
    path('get/<int:id>',todo_get),
    path('put/<int:id>',todo_put),
    path('delete/<int:id>',todo_delete),
    path('create/<int:id>',todo_create)
]
