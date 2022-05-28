from email import message
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture,Location,Category

# Create your views here.
def welcome(request):
    pictures=Picture.objects.all()
    kenya=Picture.filter_by_location(location='Kenya')
    ethiopia=Picture.filter_by_location(location='Ethiopia')
    rwanda=Picture.filter_by_location(location='Rwanda')
    southafrica=Picture.filter_by_location(location='SouthAfrica')
    return render(request, 'all-pictures/index.html', {'pictures':pictures,'kenya':kenya,'ethiopia':ethiopia,'rwanda':rwanda,'southafrica':southafrica})

def search_results():
    if 'picture' in request.GET and request.GET["picture"]:
        search_term=request.GET.get("picture")
        searched_pictures=Picture.search_by_category(search_term)
        message=f"{search_term}"
        return render(request, 'all-pictures/search.html',{"message":message,"pictures": searched_pictures})
    else:
        message = "You haven't searched for any picture"
        return render(request, 'all-pictures/search.html',{"message":message})