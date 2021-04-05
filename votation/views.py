from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from votation.models import UserEncrypted, django_system
# Create your views here.
from cryptography.fernet import Fernet
import hashlib

ownKey = 'nt45Pma7FexZ_L6fZU9wrNdVaE9eyvz4xbQ1ktdXxFk='


def encryptData(text: str) -> bytes:
    fernet = Fernet(ownKey)
    return str(fernet.encrypt(text.encode()))[2:-1]


def decryptData(text: str) -> str:
    fernet = Fernet(ownKey)
    text = text.encode()
    return fernet.decrypt(text).decode()


def hashMsg(msg: str) -> str:
    m = hashlib.shake_256()

    m.update(msg.encode('utf-8'))

    key = '0'+str(m.hexdigest(11))

    return key


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


def registerUser(request):
    userName = request.POST['userName']
    password = request.POST['password']

    if(django_system.objects.filter(name=userName).count() == 0):
        user = django_system()
        user.name = userName
        user.password = password
        user.save()

        eUser = UserEncrypted()
        eUser.id = user.id
        eUser.name = hashMsg(user.name)
        eUser.password = hashMsg(user.password)
        eUser.save()
        return JsonResponse({"msg": "User registered 👍🏻"}, status=200)

    return JsonResponse({"msg": "Username is already registered ⛔"}, status=200)


def realTime(request):
    return render(request, 'realTime.html', {})


def saveVote(request):
    votant = django_system.objects.get(name=request.session['userName'])
    votant.vote = request.GET['party']
    votantB = UserEncrypted.objects.get(id=votant.id)
    votantB.vote = hashMsg(request.GET['party'])
    votantB.save()
    votant.save()
    return JsonResponse({}, status=200)


def requestUpdate(request):
    workersVotes = django_system.objects.filter(vote="worker").count()
    scientificVotes = django_system.objects.filter(vote="scientific").count()
    democratVotes = django_system.objects.filter(vote="democrat").count()
    return JsonResponse({"workersVotes": workersVotes, "scientificVotes": scientificVotes,
                         "democratVotes": democratVotes}, status=200)
