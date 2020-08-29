from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from django.contrib.auth import authenticate



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# def dashboard_view(request,string):

# @permission_classes((IsAuthenticated, ))
# permission_classes = [IsAuthenticated, ]

def dashboard_view(request,string):
    permission_classes = (IsAuthenticated, )
    

    url = "https://192.168.107.11:8585/auth"
    headers = {'content-type': 'application/json'}

    body={
		'username' : 'exapiuser1',
		'password' : 'exAPI@user1'
	}
    r=requests.post(url, data=json.dumps(body), headers=headers)
    decoded_hand = json.loads(r.text)
    #print(decoded_hand['access_token'])


    
    headers_final={
    'authorization': 'JWT '+decoded_hand['access_token']
    }
    
    url = "https://192.168.107.11:8585/account/"+string
    r_final=requests.get(url,headers=headers_final)
    
    return HttpResponse(r_final.text,content_type='application/json')
