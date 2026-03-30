from django.urls import path
from . import views

urlpatterns = [
    path("members/", views.members, name="members"),
    path("mypage/", views.members, name="mypage"),
    path("numbers/", views.number_view, name="number_view"),
    path("form/", views.form_c, name="form_c"), 
]