from django.shortcuts import render

# Create your views here.
def ingredients(request):
    return render (request, 'ingredients.html')
