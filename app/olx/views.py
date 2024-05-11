
from django.shortcuts import render,redirect
from olx.models import vehicle
from olx.forms import vehicleform
# to register user
from django.contrib.auth.models import User
# for authentication validation
from django.contrib.auth import authenticate,login,logout
# to pass value in text
from django.http import HttpResponse

# Create your views here.


def register(request):
    """  register a new user in django User table """
    if (request.method == "POST"):  # Check if the form is submitted
        u = request.POST['username']
        p = request.POST['password']
        cp = request.POST['confirmpassword']
        e=request.POST['email']
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        if(cp==p):
            user = User.objects.create_user(username=u,password=p,email=e,first_name=fn,last_name=ln,)
            user.save()
            return redirect('home')
        else:
            return HttpResponse("Password are not the same")
    return render(request,'Register.html')


def user_login(request):
    """ login validation code in django """
    if(request.method=="POST"):
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        """ checking the user name and password correct or not """
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Credintial")
    return render(request,'Login.html')


def user_logout(request):
    """ user logout function """
    logout(request)
    return user_login(request)

def home(request):
    s = vehicle.objects.all()
    print(s)
    return render(request, 'home.html',{'v':s})
def details(request,n):
    b=vehicle.objects.get(id=n)
    return render(request,'viewdetails.html',{'b':b})
def register_vehicle(request):
    if request.method == "POST":
        model_type = request.POST['model_type']
        model_name = request.POST['model_name']
        year = request.POST['year']
        price = request.POST['price']
        image = request.FILES.get('image')  # Access uploaded image file

        v = vehicle.objects.create(model_type=model_type, model_name=model_name, year=year, price=price, image=image)
        v.save()
        return render(request,'home.html')  # Assuming 'home' is the name of your home page URL pattern
    else:

        return render(request, 'add.html')

def edit(request,d):

    b = vehicle.objects.get(id=d)
    if (request.method == "POST"):
        form = vehicleform(request.POST, request.FILES, instance=b)
        if form.is_valid():
            form.save()
            return details(request,n=d)
    form = vehicleform(instance=b)
    return render(request,'edit.html',{'form':form})
def delete(request,d):
    b = vehicle.objects.get(id=d)
    b.delete()
    return render(request,'home.html')

