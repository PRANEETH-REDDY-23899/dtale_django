from django.shortcuts import render,HttpResponse
from .forms import CsvModelForm
from .models import Csv
import pandas as pd
from django.shortcuts import redirect,render
from dtale.views import startup
from django.conf import settings
# Create your views here.

def upload_view(request):
    form = CsvModelForm(request.POST or None,request.FILES or None )
    if form.is_valid():
        form.save()
        form=CsvModelForm()
    return render(request,'base/upload.html',{'form':form})

def create_df(request):
    obj=Csv.objects.latest('id')
    df=pd.read_csv(obj.file_name.path)
    instance = startup(data=df, ignore_duplicate=True)
    resp = redirect(f"/flask/dtale/main/{instance._data_id}")
        # print(resp)
    return resp

