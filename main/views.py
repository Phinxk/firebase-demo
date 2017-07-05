from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'message': 'This is a Firebase Cloud Message Demo!'
    }
    return render(request, 'main/home.html', context)
