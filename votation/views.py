from django.shortcuts import redirect, render
from votation.models import UserEncrypted, django_system
# Create your views here.


def login(request):
    return render(request, 'login.html', {})


def logout(request):
    if 'userName' in request.session.keys():
        del request.session['userName']
    return render(request, 'login.html', {})


def vote(request):
    userName = request.POST['userName']
    password = request.POST['password']
    matches = django_system.objects.filter(name=userName)
    if(matches.count() == 1 and django_system.objects.get(name=userName).password == password):
        resultUser = django_system.objects.get(name=userName)
        request.session['userName'] = resultUser.name
        return render(request, "vote.html", {'userName': resultUser.name, 'vote': resultUser.vote})
    else:
        return redirect('login')


def realTime(request):
    return render(request, 'realTime.html', {})
