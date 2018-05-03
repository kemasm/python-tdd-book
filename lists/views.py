from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
	response = '<html><title>To-Do lists</title></html>'
	return HttpResponse(response)
