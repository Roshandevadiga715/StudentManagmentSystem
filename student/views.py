from django.shortcuts import render
from.forms import StudForm,SForm
from.models import student

# Create your views here.
def show(request):
    return render(request,"home.html")

def register(request):
    title = "Student Registration"
    form = StudForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['s_name']
        clas = form.cleaned_data['s_class']
        addr = form.cleaned_data['s_address']
        school = form.cleaned_data['s_school']
        mail = form.cleaned_data['s_email']
        email = student.objects.filter(s_email=mail)
        if len(email)>0:
            return render(request,'ack.html',{"title":"Student Already exists... Try with other E-mail"})
        else:
            p = student(s_name=name,s_class=clas,s_address=addr,s_school=school,s_email=mail)
            p.save()
            return render(request,'ack.html',{"title":"Registered Successfully"})
            
    context={
    "title":title,
     "form":form,
    }
    return render(request,'register.html',context)

def existing(request):
    title="All Registered students"
    queryset= student.objects.all()
    context={
    "title":title,
    "queryset":queryset,
    }
    return render(request,"existing.html",context)

def Search(request):
    title="Search Student"
    form=SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        queryset = student.objects.filter(s_name=name)
        if len(queryset)==0:
            return render(request,'ack.html',{'title':"Student details Not found... please enter correct data"})


        context={
        'title':title,
        'queryset':queryset,
        }
        return render(request,'existing.html',context)
        
    
    context = {
    'title':title,
    'form':form,
    }
    return render(request,'Search.html',context)

def Dropout(request):
    title="Drop Out"
    form=SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['s_name']
        queryset = student.objects.filter(s_name=name)
        if len(queryset)==0:
            return render(request,'ack.html',{'title':"Student details Not found... please enter correct data"})
        else:
            queryset = student.objects.filter(s_name=name).delete()
            return render(request,'ack.html',{'title':"Student removed from your database"})
    context = {
    'title':title,
    'form':form,
    }
    return render(request,'Search.html',context)