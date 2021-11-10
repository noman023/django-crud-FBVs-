from django.shortcuts import render, HttpResponseRedirect
from myapp.forms import PlayerForm
from myapp.models import Player
from django.contrib import messages
# Create your views here.
def home(request):
    data = Player.objects.all()

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Submition Is Accepted !')
            # messages.SUCCESS(request, 'Your Submition Is Accepted !')
            form = PlayerForm()
    else:
        form = PlayerForm()

    return render(request, 'myapp/home.html', {'form':form, 'data':data})

def delete(request, jersey_no):
    pi = Player.objects.get(pk=jersey_no)
    pi.delete()
    return HttpResponseRedirect('/')

def update(request,jersey_no):
    if request.method == 'POST':
        pi = Player.objects.get(pk=jersey_no)
        fm = PlayerForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Player.objects.get(pk=jersey_no)
        fm = PlayerForm(instance=pi)
    return render(request, 'myapp/update.html', {'form':fm})

