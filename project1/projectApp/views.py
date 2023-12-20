from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import team


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    jp = team.objects.all()

    return   render(request,"index.html",{'result':obj,'result1':jp})








# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x + y
#     p = x - y
#     k = x/y
#     t = x*y
#
#     return  render(request,"about.html",{'result':res})
