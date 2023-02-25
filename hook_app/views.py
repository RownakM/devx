from django.http import HttpResponse
from django.shortcuts import render
import git,os

from devx.settings import BASE_DIR
# Create your views here.
def pullGithub(request):
    # if request.method=="POST":
    repo=git.Repo(BASE_DIR)
    origin=repo.remotes.origin

    origin.pull()
    return HttpResponse("OK")