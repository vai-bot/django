from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib import messages
from .models import MyTable


def members(request):
  template = loader.get_template("myfirst.html")
  return HttpResponse(template.render()) 

def number_view(request):
  numbers=[1,2,3,4,5]
  return render(request, "numbers.html", {"numbers": numbers})


def Insert_Data(request):
  if request.method=="POST":
    name=request.POST.get("name")
    subject=request.POST.get("subject")
    email=request.POST.get("email")

    try:
      MyTable.objects.create(name=name, subject=subject, email=email)
      messages.success(request, "Data insert successfully")

    except IntegrityError:
      messages.error(request, "Email already exist")
      return render(request, "form.html", {"error": "Email already exists"})
    return redirect("insert")
  return render(request, "form.html")

def values(request):
  mymembers = MyTable.objects.all()

  template=loader.get_template("all_members.html")

  context={
    "mymembers" : mymembers,
  }
  return HttpResponse(template.render(context,request))