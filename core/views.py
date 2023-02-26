from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from core.models import Application, Colleges
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


@api_view(['POST'])
def application(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        whatsapp_number=request.POST['wp_no']
        college_id=request.POST['college_id']
        linkedin=request.POST.get('linkedin',None)
        github=request.POST.get('github',None)
        question=request.POST['question']
        meal_type=request.POST['meal_type']
        tshirt_size=request.POST['tshirt_size']

        Application.objects.create(name=name,email=email,whatsapp_number=whatsapp_number,college=Colleges.objects.get(college_id=college_id),linkedin=linkedin,github=github,question=question,meal_type=meal_type,tshirt_size=tshirt_size)

        return Response({'message':'Created'},status=status.HTTP_201_CREATED)


@api_view(['GET'])
def listColleges(request):
    import requests

    url = "https://university-college-list-and-rankings.p.rapidapi.com/api/universities"

    querystring = {"countryCode":"in"}

    headers = {
        "X-RapidAPI-Key": "f834edffa9msh2e26e78a525559bp1e4006jsn1ab53a8adaa0",
        "X-RapidAPI-Host": "university-college-list-and-rankings.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_json=response.json()

    result=response_json['data']['rankings']

    for i in range(1,len(result)):
        db=result[str(i)]
        Colleges.objects.create(college_id=db["id"],location=db["location"],name=db["name"])

    return Response({"OK":"OK"})