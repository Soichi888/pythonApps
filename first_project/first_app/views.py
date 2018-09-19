from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	data_dict = {'access_records':webpages_list}
	return render(request,'first_app/index.html', context=data_dict)


def help(request):
	print(reverse('help'))
	# my_dict = {'insert_me': "Some update"}
	# return render(request,'first_app/index.html', context=my_dict)
	return HttpResponse("This is help page")
