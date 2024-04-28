from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ManageGroupForm
from .models import User
# Create your views here.

def view_users_in_group(request):
    if request == 'GET':
        form = ManageGroupForm(request.POST, request.FILES)
        users = User.objects.all()
        
        if form.is_valid():
            form.save()

        return render(request, "view_users_in_group.html", {'form': form}, {'users': users})

    
    if request == 'GET':
        return render(request, "view_users_in_group.html", {'form': form})
    
    if request == 'POST': # if you add/delete users
        form = ManageGroupForm(request.POST, request.FILES)
        users = User.objects.all()
        
        if form.is_valid():
            form.save()

        return render(request, "view_users_in_group.html", {'form': form}, {'users': users})
    
    return HttpResponse("groups listed here:")