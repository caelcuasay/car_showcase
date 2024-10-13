from django.shortcuts import render

def index(request):
    return render(request, 'porsche/index.html')

def gallery(request):
    return render(request, 'porsche/gallery.html')

def specs(request):
    return render(request, 'porsche/specs.html')
