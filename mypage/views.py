from django.shortcuts import render
from .models import Dog


def dog_views(request):
    dogs = Dog.objects.all()
    return render(request,'index.html',{'dogs':dogs})


def dog_detail(request,breed_name):
    try:
        dog = Dog.objects.get(Breed=breed_name)
    except Dog.DoesNotExist:
        return render(request,'dog_not_found.html')
    
    return render(request,'dog_detail.html',{'dog':dog})

def about_views(request):
    return render(request,'about.html')