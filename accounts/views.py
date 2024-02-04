from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .forms import SignupForm ,UserCreationForm
from .models import Profile
# Create your views here.

def signup(request):
    '''
    create new user, profile
    send email with code
    redirect user to activate code
    '''

    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save(commit=True)
            # how i can access user befor save(i don't have user yet) i have user creation form
            user.is_active = False
            form.save()            #--------> trigger signals(create profile code) why?? as i create user
            
            profile =Profile.objects.get(user__username = username)
            #send email 
            send_mail(
                "Activate Your email",
                f"Welcome{username} \nUsing this{profile.code} to activate your Account",
                "pythondevloper33@gmail.com",
                [email],
                fail_silently=False,
            )
            

            return redirect(f'/accounts/{username}/activate')
    else:
        form = SignupForm()
    
    return render(request , 'accounts/singup.html',{'form':form})


def user_activate(request,user_name):
    '''
        activate code
        redirect to login

    '''
    
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            profile = Profile.objects.get(user__user_name = user_name)
            if profile.code ==code :
                profile.code = ''
                user = User.objects.get(user_name = user_name)
                user.is_active = True

                user.save()
                profile.save()
                return redirect('accounts/login.html')


    else:
        form = UserCreationForm()
    
    return render(request , 'accounts/activate.html',{'form':form})

