from django.shortcuts import render

# Create your views here.
def birds(request):
    return render(request,'birds.html',)