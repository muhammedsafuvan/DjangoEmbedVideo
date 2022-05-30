from django.shortcuts import render
from .models import Video
# Create your views here.
def index(request):
    Videos = Video.objects.all()
    return render(request,'videos/index.html',context={"videos":Videos})

