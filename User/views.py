# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from Service.user_service import User_Service
from Service.json_service import Json_Service
import json, datetime

'''
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        #elif isinstance(obj, date):
        #    return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
'''

def register(request):
    state, msg, data = User_Service.register(request.GET.get('userID'), request.GET.get('password'))
    json_data = Json_Service.combination(state=state, msg=msg, data=data)
    return HttpResponse(json.dumps(json_data))

def verification(request):
    state, msg, data = User_Service.verification(request.GET.get('userID'), request.GET.get('password'))
    json_data = Json_Service.combination(state=state, msg=msg, data=data)
    return HttpResponse(json.dumps(json_data))

def resetPassword(request):
    state, msg, data = User_Service.resetPassword(request.GET.get('userID'), request.GET.get('latestPassword'), request.GET.get('token'))
    json_data = Json_Service.combination(state=state, msg=msg, data=data)
    return HttpResponse(json.dumps(json_data))

def resetPersonalInfo(request):
    state, msg, data = User_Service.resetPersonalInfo(userID=request.GET.get('userID'),
                                                      token=request.GET.get('token'),
                                                      nickname=request.GET.get('nickname',''),
                                                      profile=request.GET.get('profile',''),
                                                      gender=request.GET.get('gender', ''),
                                                      bloodType=request.GET.get('bloodType', ''),
                                                      birthday=request.GET.get('birthday', ''),
                                                      address=request.GET.get('address', ''),
                                                      email=request.GET.get('email', ''))
    json_data = Json_Service.combination(state=state, msg=msg, data=data)
    return HttpResponse(json.dumps(json_data))

def getPersonalInfo(request):
    state, msg, data = User_Service.getPersonalInfo(request.GET.get('callerID'), request.GET.get('targetID'), request.GET.get('token'))
    json_data = Json_Service.combination(state=state, msg=msg, data=data)
    return HttpResponse(json.dumps(json_data))

def logout(request):
    state, msg, data = User_Service.logout(request.GET.get('userID'), request.GET.get('token'))
    json_data = Json_Service.combination(state=state, msg=msg, data=data)
    return HttpResponse(json.dumps(json_data))