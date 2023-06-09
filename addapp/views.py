from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    x=request.POST["G1"]
    y=request.POST["G2"]
    i=int(x)
    j=int(y)
    z=i+j
    res=HttpResponse("THE SUM IS:"+str(z))
    return res