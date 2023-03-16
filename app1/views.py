from django.shortcuts import render

# Create your views here.
def animal(request):
    return render(request,'animal.html',)