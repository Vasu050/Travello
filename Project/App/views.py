from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def abc(request):
   ''' return HttpResponse('hello world')   # <h1>hello world </h1>'''
   # return render(request,'home.html')
   return render(request,'app.html',{'name':'Navin'})

def add(request):
   val1=int(request.POST["num1"])  
   val2=int(request.POST["num2"])
   res=val1+val2
   return render(request,'result.html',{'result':res})