from django.shortcuts import render, HttpResponse

# Create your views here.
def coursesHome(request):
    return render(request, 'courses/index.html')