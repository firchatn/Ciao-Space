from django.shortcuts import render, get_object_or_404
from accounts.models import User
from accounts.forms import UserForm
from .forms import PostForm
from .forms import MessageForm
from .models import Post, Message, Checkin
from django.utils import timezone
from decimal import *
from django.shortcuts import redirect


locx = ""
locy = ""
vx = 0
vy = 0


def contrainer(request, urlloc):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            compte = form.save()
            cheekin_v = Checkin()
            doc = urlloc.split("a")
            locx = doc[0].replace("p", ".")
            locy = doc[1].replace("p", ".")
            cheekin_v.username = User.objects.get(username=compte.username)
            cheekin_v.x = Decimal(locx)
            cheekin_v.y = Decimal(locy)
            cheekin_v.cheek_date = timezone.now()
            cheekin_v.save()
            request.session['username'] = newuser.id
    # compte = User.objects.all()[User.objects.count()-1]
    compte = User.objects.get(id=request.session['username'])
    cheekin_compte = Checkin.objects.get(username=compte)
    cheekin_view = Checkin.objects.all().order_by('-cheek_date')
    vx = float(cheekin_compte.x)
    vy = float(cheekin_compte.y)
    aux = []  # user in space of 2km of your current compte
    for d in cheekin_view:
        m = float(d.x)
        n = float(d.y)
        if vx - 0.2 < m < vx + 0.2 and vy - 0.2 < n < vy + 0.2:
            f = User.objects.filter(username=d.username)
            aux.append(f)
    return render(request, 'space/index.html', {
        'vuser': aux, 'last': compte, 'cheekin': cheekin_view, 'x': urlloc})


def profil(request, urlloc, userspace):
    usee = User.objects.get(username=userspace)
    compte = User.objects.all()[User.objects.count() - 1]
    postt = Post.objects.all().order_by('-post_date')
    msgg = Message.objects.all().order_by('-msg_date')
    nbmsg = Message.objects.filter(toUser=usee).count()
    nbpost = Post.objects.filter(username=usee).count()
    print(nbmsg)
    return render(request, 'space/profil.html', {
        'vuser': usee, 'msg': msgg, 'last': compte, 't': urlloc,
        'postt': postt, 'nbmsg': nbmsg, 'nbpost': nbpost})


def new_post(request, urlloc, userspace):
    user = get_object_or_404(User, username=userspace)
    if request.method == "POST":
        post = Post(username=user)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    compte = User.objects.all()[User.objects.count() - 1]
    postt = Post.objects.all().order_by('-post_date')
    return render(request, 'space/post.html', {
        'form': form, 'compte': compte, 't': urlloc, 'postt': postt})


def message(request, urlloc, userspace):
    usee = get_object_or_404(User, username=username)
    compte = User.objects.all()[User.objects.count() - 1]
    cheekin_compte = Checkin.objects.all()[Checkin.objects.count() - 1]
    cheekin_view = Checkin.objects.all().order_by('-cheek_date')
    vx = float(cheekin_compte.x)
    vy = float(cheekin_compte.y)
    aux = []
    for d in cheekin_view:
        m = float(d.x)
        n = float(d.y)
        if vx - 0.2 < m < vx + 0.2 and vy - 0.2 < n < vy + 0.2:
            f = User.objects.filter(username=d.username)
            aux.append(f)
    if request.method == "POST":
        for i in aux:
            for j in i:
                if j.username in request.POST:
                    to = request.POST[j.username]
        toUser = User.objects.get(username=to)
        message = Message(fromUser=userspace, toUser=toUser)
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            newmsg.save()
    else:
        form = MessageForm()
    return render(request, 'space/message.html', {
        'form': form, 'vuser': usee, 'last': compte,
        't': urlloc, 'vuser2': aux})


def logout(request):
    request.session[0] = 'logout'
