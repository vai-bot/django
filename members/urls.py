from django.urls import path
from . import views

urlpatterns = [
    path("members/", views.members, name="members"),
    path("mypage/", views.members, name="mypage"),
    path("numbers/", views.number_view, name="number_view"),
    path("form/", views.Insert_Data, name="insert"), 
    path("values/" ,views.values, name="values"),
    path("show/", views.show_data, name="show_data"),
    path("delete/<int:id>/", views.delete_data, name="delete"),
]