from django.shortcuts import render

def index(request):
    return render(request, 'gtr/index.html')

def gallery(request):
    return render(request, 'gtr/gallery.html')

def specs(request):
    return render(request, 'gtr/specs.html')

def landing_page(request):
    return render(request, 'gtr/landing_page.html')
