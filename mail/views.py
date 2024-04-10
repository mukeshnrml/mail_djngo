from django.core.mail import send_mail
from django.shortcuts import render


def home(request):
    send_mail(
        "Test Mail", # sub 
        "This mail sended by Django",  # msg Body
        "nirmalmukesh2000@gmail.com",# sender mail
        ["mukeshnirmal@outlook.com"], # recvier mail
        fail_silently=False,
        )
    return render(request,'index.html')

    