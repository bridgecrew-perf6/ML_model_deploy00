from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def home (request):
	return render (request , 'home.html',{})

# def register(request):
# 	form = UserCreationForm()
# 	return render(request ,'register/signup.html',{})
@login_required
def main(request):
	return render(request,'main.html',{})


def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
		return redirect("/login")
	else:
		form = RegisterForm()

	return render(response, "registration/signup.html", {"form":form})