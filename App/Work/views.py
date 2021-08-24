from django.shortcuts import render , redirect
from .models import  ContactOffice , Lost , Found
from .forms import LostForm , FoundForm
from django.contrib import messages

ContactList = ContactOffice.objects.all()
ApprovedLost = Lost.objects.filter(Status='Approved')
ApprovedFound = Found.objects.filter(Status='Approved')
# Create your views here.
def index(request):
    return render(request , 'Work/index.html' , {"ContactList" : ContactList ,  "ApprovedLost" : ApprovedLost  , "ApprovedFound" : ApprovedFound})

def lost(request):
    if request.method == "GET":
        return render(request , 'Work/Lost.html' ,{"Lost" : LostForm} )

    if request.method == "POST":
        form = LostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'OK!! Your Lost Report Send Successfully.')
            form = LostForm()
            return render(request , 'Work/Lost.html' , {"Lost" : form})
        else:
            return render(request , 'Work/Lost.html' ,{"Lost" : form})


def found(request):
    if request.method == "GET":
        return render(request , 'Work/Found.html' ,{"Found" : FoundForm} )

    if request.method == "POST":
        form= FoundForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'OK!! Your Found Report Send Successfully.')
            form = FoundForm()
            return render(request , 'Work/Found.html' , {"Found" : form})
        else:
            return render(request , 'Work/Found.html' ,{"Found" : form})
