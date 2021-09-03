import pandas as pd
from django.shortcuts import redirect,render
from dtale.views import startup
from django.conf import settings
from django.core.files.storage import FileSystemStorage



def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, './index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, './index.html')

   
def create_df(request):
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    df=pd.read_csv("http://localhost:8000"+uploaded_file_url)
    instance = startup(data=df, ignore_duplicate=True)
    resp = redirect(f"/flask/dtale/main/{instance._data_id}")
    return resp

