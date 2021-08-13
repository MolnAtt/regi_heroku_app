from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def VIEW(request):
    return render(request, "teszt.html", {})
