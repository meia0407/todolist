from django.urls import path
from . import views
<<<<<<< HEAD
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete

urlpatterns = [
    path("", TodoList.as_view(), name="list"),
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
    path("create/", TodoCreate.as_view(), name="create"),
    path("update/<int:pk>", TodoUpdate.as_view(), name="update"), 
    path("delete/<int:pk>", TodoDelete.as_view(), name="delete"), 
=======
from .views import TodoList

urlpatterns = [
    path("", TodoList.as_view(), name="list"),
>>>>>>> 04f7a03bae29b79cf4e1a17a3ab241a394bc02cb
]