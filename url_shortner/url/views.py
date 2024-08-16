from django.shortcuts import render
from django.http import HttpResponse
from .models import link
import uuid

# Create your views here.

def shorten(request):
    input = link()
    try:
        if(request.method == "POST"):
            input.address = request.POST.get("url")
            input.aid = str(uuid.uuid4())[:6]
            input.save()
        data = {
            "url_link": input.address,
            "output": input.aid,
            }
        print(data)
        return render(request,"index.html",data)
    except Exception as e:
            print("Error:", e)
            return render(request, "index.html", {"error": "An error occurred while processing your request."})