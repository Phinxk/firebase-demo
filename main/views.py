import json
import requests

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'message': 'This is a Firebase Cloud Message Demo!'
    }
    return render(request, 'main/home.html', context)


@csrf_exempt
def register_device(request):
    message = "Error"
    if request.is_ajax() and request.method == 'POST':
        token = request.POST.get('token')
        message = "Success"
        headers = {
            'content-type': 'application/json',
            'authorization': 'key={}'.format(settings.FIREBASE_TOKEN)
        }

        data = {}

        url = 'https://iid.googleapis.com/iid/v1/{}/rel/topics/tests'.format(token)

        json_data = json.dumps(data)
        response = requests.post(url, data=json_data, headers=headers)
        print(response.status_code, response.content)
    return HttpResponse(message)

@csrf_exempt
def delete_device(request):
    message = "Error"
    if request.is_ajax() and request.method == 'POST':
        token = request.POST.get('token')
        message = "Success"
        headers = {
            'content-type': 'application/json',
            'authorization': 'key={}'.format(settings.FIREBASE_TOKEN)
        }

        data = {}

        url = 'https://iid.googleapis.com/v1/web/iid/{}'.format(token)

        json_data = json.dumps(data)
        response = requests.delete(url, data=json_data, headers=headers)
        print(response.status_code, response.content)
    return HttpResponse(message)
