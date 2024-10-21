from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request): 
  
   '''dest1=Destination()
   dest1.name='Mumbai'
   dest1.desc="city that never sleeps"
   dest1.price=700
   dest1.image='destination_1.jpg'  # do 'images/destination_1.jpg' if want to access dynamic image directly
   dest1.offer=True

   dest2=Destination()
   dest2.name='thailand'
   dest2.desc="city that never let sleep"
   dest2.price=800
   dest2.image='destination_2.jpg'
   dest2.offer=False

   dest3=Destination()
   dest3.name='lakshdweep'
   dest3.desc="oceans"
   dest3.price=900
   dest3.image='destination_3.jpg'
   dest3.offer=False

   dests=[dest1,dest2,dest3]'''   # when data is static or passed by programmer not database
   dests= Destination.objects.all()
   return render(request,'index.html',{'dests':dests})  


def about(request):
   return render(request,'about.html')


