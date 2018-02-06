from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context=context_dict)
def about(request):
	return HttpResponse('rango says this is the about page')  

def rangImage(request):
	return HttpResponse('rango says here is the immage')   

# Create your views here.
