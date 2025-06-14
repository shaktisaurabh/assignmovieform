from django.shortcuts import render,redirect
from assignmodformapp.forms import projectform
from assignmodformapp.models import project
# Create your views here.
def index(request):
    return render(request,'assignmodformapp/index.html')
def listprojects(request):
    projects=project.objects.all()
    return render(request,'assignmodformapp/listprojects.html',{'projects':projects})
def addproject(request):
    if request.method=="POST":
        form=projectform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = projectform()
    return render(request,'assignmodformapp/addproject.html',{'form':form})
    
