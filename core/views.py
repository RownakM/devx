from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def home(request):
    return Response({"status":status.HTTP_200_OK})

@api_view(['GET'])
def verify_google(request):
    token=request.GET['token']
    from google.oauth2 import id_token
    from google.auth.transport import requests
    try:
    # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), "617427136394-cun1fis2l9inm34vhkv0ejo535r1vhm5.apps.googleusercontent.com")

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
        return Response({'userid':userid})
    except ValueError:
        # Invalid token
        return Response({'error':"valueerror"})