from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from app1.models import Patches
from app1.serializers import PatchesSerializer

from django.core.files.storage import default_storage
import requests

from django.http import HttpResponse
from bs4 import BeautifulSoup
from .forms import UrlForm

import csv


@csrf_exempt
def patchesApi(request,id=0):
    if request.method=='GET':
        patches = Patches.objects.all()
        patches_serializer=PatchesSerializer(patches,many=True)
        return JsonResponse(patches_serializer.data,safe=False)

    #for testing
    elif request.method=='POST':
        patches_data=JSONParser().parse(request)
        patches_serializer=PatchesSerializer(data=patches_data)
        if patches_serializer.is_valid():
            patches_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
        
    elif request.method=='DELETE':
        Patches.objects.all().delete()
        return JsonResponse("delete complete",safe=False)



def disp(request):
    if request.method=='GET':
        form = UrlForm()
        patches = Patches.objects.all()
        return render(request,'index4.html',{'response':patches,'form':form})

    #load from url
    elif request.method=='POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            print(url)
        else:
            #url = "https://www.oracle.com/security-alerts/cpujan2023.html"
            url = "err"

        try:

            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            objs=[]

            tables = soup.find_all("table")
            for i in range(2,17):
                table = tables[i]
                tbody = table.find("tbody")
                rows = tbody.find_all("tr")
                for row in rows:
                    cells = row.find_all("td")
                    cells2 = row.find_all("th")
                    data2 = [cell.text for cell in cells2]
                    data = [cell.text for cell in cells]
                    data =[*data2,*data]
                    print(data)
                    objs.append(Patches(col0=data[0], col1=data[1],col2=data[2],col3=data[3], col4=data[4],col5=data[5],col6=data[6],
                    col7=data[7],col8=data[8],col9=data[9], col10=data[10],col11=data[11],col12=data[12],col13=data[13], col14=data[14]))
                    
            Patches.objects.bulk_create(objs) 
        
            return redirect('/')

        except:
            return JsonResponse("something went wrong.check url",safe=False)


