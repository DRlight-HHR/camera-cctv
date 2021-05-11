from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from random import randrange
from django.conf import settings

from rest_framework.authtoken.models import Token

passlist = [52608088]
check_limit = [0]
u_s_e_r = ['amir', 'amir', 'amir']


def sendmail(_name, _mail):
    ran = randrange(1000000, 10000000)
    subject = 'ساخت حساب:'
    message = "{0} عزیز رمز شما جهت ساخت حساب در سایت عبارت اند از {1}".format(_name, ran)
    send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[_mail])
    return ran


def check(request):
    if request.user.is_authenticated is True:
        return redirect('book/main/home/')
    if request.method == 'POST':
        global passlist
        get_pass = request.POST.get('__pass__')
        get_pass = int(get_pass)
        if get_pass != passlist[0]:
            if check_limit[0] == 3:
                return redirect('/')
            error = {"error": "رمزی که وارد کرده اید اشتباه است دوباره وارد کنید"}
            check_limit[0] = check_limit[0] + 1
            return render(request, 'check.html', error)
        else:
            global u_s_e_r
            user = User.objects.create_user(username=u_s_e_r[0], password=u_s_e_r[1], email=u_s_e_r[2])
            user_check = authenticate(request=request, username=u_s_e_r[0], password=u_s_e_r[1])
            if user_check is not None:
                login(request, user_check)
                return redirect('book/main/home/')
    return render(request, 'check.html')


def sing_up(request):
    if request.user.is_authenticated is True:
        return redirect('/book/main/home/')
    else:
        if request.method == 'POST':
            _username_ = request.POST.get('_username_')
            _fullname_ = request.POST.get('_name_')
            _email_ = request.POST.get('_email_')
            _pass1_ = request.POST.get('_pass1_')
            _pass2_ = request.POST.get('_pass2_')
            if _username_ == "" or _fullname_ == "" or _email_ == "" or _pass1_ == "" or _pass2_ == "":
                error = {"error": "فیلد ها نباید خالی باشند"}
                return render(request, 'Singup.html', error)
            else:
                username = User.objects.filter(username=_username_)
                email = User.objects.filter(email=_email_)
                if username.exists():
                    _error = {"username_error": "نام کاربری که انتخاب کرداید موجود است لطفا نام کاربری دیگری وارد کنید"}
                    return render(request, 'Singup.html', _error)
                elif email.exists():
                    _error_ = {
                        "email_error": "ایمیلی که وارد کرده اید قبلا انتخاب شده است یا وارد شوید یا از ایمیل دیگری استفاده کنید"}
                    return render(request, 'Singup.html', _error_)
                else:
                    pa = sendmail(_fullname_, _email_)
                    global passlist, u_s_e_r
                    passlist[0] = pa
                    u_s_e_r[0] = _username_
                    u_s_e_r[1] = _pass1_
                    u_s_e_r[2] = _email_
                    return redirect('/check/')

        return render(request, 'Singup.html')


def log_in(request):
    if request.user.is_authenticated is True:
        return redirect('/book/main/home/')
    if request.method == 'POST':
        u = request.POST.get('_username_')
        p = request.POST.get('_pass1_')
        user_check = authenticate(request, username=u, password=p)
        '''token = Token.objects.get(user=user_check).key
        print(token)'''
        if user_check is not None:
            login(request, user_check)
            return redirect('/book/main/home/')
        else:
            return HttpResponse('bad request')
    else:
        return render(request, 'Login.html')


def log_out(request):
    logout(request)
    return redirect('/login/')


def home_(request):
    if request.user.is_authenticated is False:
        return redirect('/login/')
    else:
        return render(request, 'book_home.html')
