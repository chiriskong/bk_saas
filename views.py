from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ad_view(request):
    return render(request,"/template/AD.html")