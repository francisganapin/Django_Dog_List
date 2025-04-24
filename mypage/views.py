from django.shortcuts import render
from .models import Dog
from django.core.paginator import Paginator

def dog_views(request):

    dogs = Dog.objects.all()
    if request.method == 'POST':
        dog_name = request.POST.get('dog_name')

        if dog_name:
            dogs = Dog.objects.filter(breed__icontains=dog_name)


    print(dogs)
    paginator = Paginator(dogs,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'dogs':dogs,'page_obj':page_obj}

    return render(request,'index.html',context)


def dog_detail(request,breed_name):
    try:
        dog = Dog.objects.filter(breed=breed_name).prefetch_related('character_traits', 'health_problems')

        #for debug show dog url
        #for item in dog:
            #item.image.url
            #print(item.image.url)

    except Dog.DoesNotExist:
        return render(request,'dog_not_found.html')
    
    return render(request,'dog_detail.html',{'dog':dog})

def about_views(request):
    return render(request,'about.html')

