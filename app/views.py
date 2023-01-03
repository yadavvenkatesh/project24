from django.shortcuts import render

# Create your views here.
def first(request):
    d={'a':10,'b':20}
    return render (request,'first.html',d)