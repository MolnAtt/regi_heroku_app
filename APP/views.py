from django.shortcuts import render

def VIEW(request):
    return render(request, "teszt.html", {})
