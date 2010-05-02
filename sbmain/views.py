from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from scrapbook.sbmain.models import *

def index(request):
    next = "/landing"
    if 'next' in request.GET:
        next = request.GET["next"]
    return render_to_response("index.html", {"next": next})

@login_required
def landing(request):
    return render_to_response("landing.html", {"user": request.user})

@login_required
def videos(request):
    videos = VideoRef.objects.all()
    return render_to_response("videos.html", {"user": request.user, "videos": videos})

@login_required
def blog(request):
    entries = BlogEntry.objects.order_by('-time')
    return render_to_response("blog.html", {"user": request.user, "blog_entries": entries})

@login_required
def galleries(request):
    galleries = Gallery.objects.all()
    return render_to_response(
        "galleries.html",
        {"user": request.user, "gallery_type": "gallery", "galleries": galleries})

@login_required
def gallery(request, galleryID):
    gallery = Gallery.objects.get(id=galleryID)
    return render_to_response("gallery.html", {"user": request.user, "gallery": gallery})

@login_required
def portraits_list(request):
    galleries = PortraitGallery.objects.all()
    return render_to_response(
        "galleries.html",
        {"user": request.user, "gallery_type": "portraits", "galleries": galleries})

def portraits(request, galleryID):
    gallery = PortraitGallery.objects.get(id=galleryID)
    return render_to_response(
        "kandids.html",
        {"user": request.user, "gallery": gallery})

@login_required
def construction(request):
    return render_to_response("construction.html", {"user": request.user})

@login_required
def landing(request):
    return render_to_response("landing.html", {"user": request.user})

def sblogin(request):
    username = request.POST['user']
    password = request.POST['pass']
    next = "/landing.html"
    if "next" in request.POST:
        next = request.POST['next']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            return render_to_response("index.html", {"error": "Authentication Failed"})
    else:
        return render_to_response("index.html", {"error": "Authentication Failed"})

def sblogout(request):
    logout(request)
    return HttpResponseRedirect("/")
