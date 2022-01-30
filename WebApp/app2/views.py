from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        x = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                     password=password)
        x.save()
        print("user created")
        return redirect('/')



    else:
        return render(request, 'b.html')

# Create your views here.
