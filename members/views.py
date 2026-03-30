from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.shortcuts import render

def members(request):
  template = loader.get_template("myfirst.html")
  return HttpResponse(template.render()) 

def number_view(request):
  numbers=[1,2,3,4,5]
  return render(request, "numbers.html", {"numbers": numbers})


def form_c(request):
    return render(request, "form.html")