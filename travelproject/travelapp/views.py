from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Place2
from django.shortcuts import render

def demo(request):
    obj = Place.objects.all()
    obj2 = Place2.objects.all()
    return render(request, "index.html", {'result': obj, 'result2': obj2})

#def addition(request):
  #  x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
 #   res1 = x + y
  #  res2 = x - y
  #  res3 = x * y
 #   res4 = x / y
  #  return render(request, "about.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})

#def contact(request):
 #   return HttpResponse("Good morning")