from django.http import HttpResponse
from django.shortcuts import render
import git
# Create your views here.
def pullGithub(request):
    # if request.method=="POST":
    repo=git.Repo('https://github.com/RownakM/devx.git')
    origin=repo.remotes.origin

    origin.pull()
    return HttpResponse("Imported Successfully")