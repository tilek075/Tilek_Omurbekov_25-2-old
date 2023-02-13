from django.shortcuts import HttpResponse
import datetime

now = datetime.datetime.now()


def hello_view(requests):
    if requests.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date_view(requests):
    if requests.method == 'GET':
        return HttpResponse(str(now))

def goodby_view(requests):
    if requests.method == 'GET':
        return HttpResponse('Goodby user')
