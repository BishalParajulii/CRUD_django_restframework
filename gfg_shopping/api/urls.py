from tkinter.font import names

from django.urls import path

from . import views

urlpatterns = [
    path('' , views.ApiOverview , name = "home"),
    path('create/' , views.add_items , name = "add-items") ,
    path('all/' , views.view_items , name = "view-items"),
    path('update/<int:pk>/' , views.update_item , name="update"),
    path('delete/<int:pk>/' , views.delete_item , name="delete")
]
