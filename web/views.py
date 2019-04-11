from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse


def signup(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password'] and request.POST['email']:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            try:
                user = User.objects.create_superuser(username, email, password)
                user.save()
                return HttpResponse('yeeeessssssssss')
            except Exception:
                return HttpResponse('این یوزری که شما انتخاب کردید قبلا وجود داشته')
        else:
            return HttpResponse('دقت کتید که همه فیلد ها پر باشند')

    else:
        return render(request, 'login.html')
