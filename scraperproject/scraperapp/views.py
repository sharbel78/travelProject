
from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from  bs4 import  BeautifulSoup
from . models import Links
# Create your views here.





def home(request):
    if request.method=="POST":
        Links_new=request.POST.get('page')
        urls=requests.get(Links_new)
        beautysoup = BeautifulSoup(urls.text,'html.parser')
    
        for link in  beautysoup.find_all('a'):
            li_address= link.get('href')
            li_name=link.string
            Links.objects.create(address=li_address,stringname=li_name)
        return HttpResponseRedirect ('/')
    else:
          date_values=Links.objects.all()
    return   render(request,'home.html',{'date_values': date_values})