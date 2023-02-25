from django.http import HttpResponse
from django.shortcuts import render
import git,os
# Create your views here.
def pullGithub(request):
    # if request.method=="POST":
    repo=git.Repo(os.getcwd())
    origin=repo.remotes.origin

    origin.pull()
    return HttpResponse("OK")