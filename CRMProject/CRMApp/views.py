from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUser,LoginUser,AddRecordForm,UpdateRecordForm
from .models import Record
from django.contrib import messages

def Homepage(request):
    
    return render(request,'Index.html')

#To register a User
def Register(request):
    
    form = CreateUser()
    
    if request.method == "POST":
        form = CreateUser(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("login")
    
    context = {'form':form}
    
    return render(request,'SignUp.html',context=context)

#Login a User
def UserLogin(request):
    form = LoginUser()
    
    if request.method == "POST":
        form = LoginUser(request, data=request.POST)
        
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect("dashboard")
                
    context = {'form':form}
    return render(request,'Login.html',context=context)

#Dashboard View
@login_required(login_url='login')
def Dashboard(request):
    
    my_records = Record.objects.all()
    context = {'records': my_records}
    
    return render(request,'Dashboard.html',context=context)

#Create/Add a Record
@login_required(login_url='login')
def CreateRecord(request):
    form = AddRecordForm()
    
    if request.method == "POST":
        form =AddRecordForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,"Your Record has been Created!!")
            return redirect("dashboard")
        
    context = {'form': form}
    return render(request,'CreateRec.html',context=context)

#Update a Record
@login_required(login_url='login')
def UpdateRecord(request,pk):
    records = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=records)
    
    if request.method == "POST":
        form = UpdateRecordForm(request.POST,instance=records)
        
        if form.is_valid:
            form.save()
            messages.success(request,"Your Record has been Updated!!")
            return redirect("dashboard")
    
    context = {'form' : form}
    return render(request,'UpdateRec.html',context=context)

#View/Read a Single Record
@login_required(login_url='login')
def ViewRecord(request,pk):
    records = Record.objects.get(id=pk)
    
    context = {'record':records}
    return render(request, 'ViewRec.html', context=context)

#Delete a Record
@login_required(login_url='login')
def DeleteRecord(request,pk):
    records = Record.objects.get(id=pk)
    
    records.delete()
    messages.success(request,"Your Record has been deleted!!")
    return redirect("dashboard")

#Logout a User
def UserLogout(request):
    
    auth.logout(request)
    
    messages.success(request,"Logged out Successfully!!")
    return redirect("login")


    
        
        
    


