from django.shortcuts import render
# from app_Two.models import User
from app_Two.forms import NewUserForm


# Create your views here.
my_dict = {
	'welcome_message':"This is the welcome message for the user",
	'help_message':"This is the help page",

}

def index(request):

	return render(request,'app_Two/index.html', context=my_dict)

def help(request):

	return render(request, 'app_Two/help.html',context=my_dict)

def user(request):
	form  = NewUserForm()
	if request.method == 'POST':
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print('Error form invalid')

	return render(request,'app_Two/signup.html',{'form':form})


	# user_list = User.objects.order_by('first_name')
	# user_dict = {'users':user_list}
	#
	# return render(request, 'app_Two/user.html', context=user_dict)

# def form_user_view(request):
# 	form = forms.FormUser()
#
#
# 	if request.method=='POST':
# 		form = forms.FormUser(request.POST)
# 		if form.is_valid():
# 			print("Validation Success!")
# 			print("First Name : " + form.cleaned_data['first_name'])
# 			print("Last Name : " + form.cleaned_data['last_name'])
# 			print("Email : " + form.cleaned_data['email'])
#
# 			User.first_name = form.cleaned_data['first_name']
# 			User.last_name = form.cleaned_data['last_name']
# 			User.email = form.cleaned_data['email']
#
# 	return render(request, 'app_Two/signup.html', {'form':form})
