from django.shortcuts import render, redirect

def index(request):
    return render(request, "main/landing.html")

def play(request):
    return redirect("/main")

def profile(request):
    return render(request, "main/profile.html")

def leaderboard(request):
    return render(request, "main/leaderboard.html")