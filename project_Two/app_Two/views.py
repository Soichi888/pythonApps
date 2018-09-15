from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
my_dict = {
	'welcome_message':"This is the welcome message for the user",
	'help_message':"This is the help page",

}

def index(request):

	return render(request,'app_Two/index.html', context=my_dict)

def help(request):

	return render(request, 'app_Two/help.html',context=my_dict)
