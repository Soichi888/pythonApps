from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
	my_dict = {'insert_me': "Some update"}
	return render(request,'first_app/index.html', context=my_dict)


def help(request):
	print(reverse('help'))
	# my_dict = {'insert_me': "Some update"}
	# return render(request,'first_app/index.html', context=my_dict)
	return HttpResponse("This is help page")
