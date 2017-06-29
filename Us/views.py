# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from .models import *
from django.shortcuts import HttpResponseRedirect

def index(request):
    #all_user = User.objects.all()

    sql = """
    select user.id,user.name,user.passwd,user.login,up.delete
    from Us_user as user, Us_userpermissin as up
    where user.id = up.user_id and up.Permission_id = 1
    """
    all_user = User.objects.raw(sql)
    return render_to_response("index.html",locals())

def register(request):
    # print 'request.method: ',request.method
    # print 'request.POST: ',request.POST
    if request.method == "POST" and request.POST:
        user = User()
        user.name = request.POST["username"]
        user.login = request.POST["loginname"]
        user.passwd = request.POST["password"]
        user.save()
        up = UserPermissin()
        up.Permission_id = 1
        up.user_id = user.id
        up.delete = "Y" #默认是不激活的，状态为 Y
        up.save()
    else:
        pass
    return HttpResponseRedirect("/index")





# Create your views here.
