from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html", {})

def urlap(request):
    return redirect('https://forms.gle/m83fFTCivQLD4KZR6')

@login_required
def valasztas(request):
    return render(request, "index.html", {})
