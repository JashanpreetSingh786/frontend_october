from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(request):
    my_dict= {'var_name':"hello guys this is views.py"}
    return render(request,'first/index.html',context=my_dict)
