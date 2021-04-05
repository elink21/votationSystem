from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from votation.models import UserEncrypted, django_system
# Create your views here.


def login(request):
    return render(request, 'login.html', {})


def logout(request):
    if 'userName' in request.session.keys():
        del request.session['userName']
    return redirect('login')


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


def saveVote(request):
    votant = django_system.objects.get(name=request.session['userName'])
    votant.vote = request.GET['party']
    votant.save()
    return JsonResponse({}, status=200)


def requestUpdate(request):
    workersVotes = django_system.objects.filter(vote="worker").count()
    scientificVotes = django_system.objects.filter(vote="scientific").count()
    democratVotes = django_system.objects.filter(vote="democrat").count()
    return JsonResponse({"workersVotes": workersVotes, "scientificVotes": scientificVotes,
                         "democratVotes": democratVotes}, status=200)
