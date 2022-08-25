from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from home.models import *
from itertools import chain
from django.db.models import Sum, F, Window

# Create your views here.
def landingpage(request):
    return render(request,'landingpage.html')

def home(request):
    if request.user.is_authenticated:    
        group = Group.objects.filter(user=request.user)
        member = HistoryMember.objects.filter(user=request.user).values_list("group__id","group__name").distinct()
        context = {'group':group,'member':member}
        return render(request,'home/index.html',context)
    else:
        return redirect('/login')

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        usernumber = request.POST['usernumber']
        password = request.POST['password']

        if len(usernumber) != 10:
            messages.error(request,'User Number Should be 10 Digit')
            return redirect('/login')
        else:
            user = authenticate(request,username=usernumber,password=password)
            print(user)
            if user is not None:
                auth_login(request,user)
                messages.success(request,"Successfully Logged In")
                return redirect('/')
            else:
                messages.error(request,'Something Went Wrong')
                return redirect('/login')
    else:
        return render(request,'home/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        usernumber = request.POST['usernumber']
        email = request.POST['email']
        password = request.POST['password']


        already_number = User.objects.filter(username=usernumber) 
        already_email = User.objects.filter(email=email)

        if len(already_number) == 1:
            messages.error(request,'User Number is Already Exists')
            return redirect('/register')

        if len(already_email) == 1:
            messages.error(request,'User Email is Already Exists')
            return redirect('/register')

        if len(usernumber) != 10:
            messages.error(request,'User Number Should be 10 Digit')
            return redirect('/register')
        else:
            user = User.objects.create_user(username=usernumber,email=email,password=password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request,"Account Successfully Created")
            return redirect('/login')

    return render(request,'home/register.html')

def logout(request):
    auth_logout(request)
    return redirect('/login')


def group(request):
    if request.user.is_authenticated:
        group = Group.objects.filter(user=request.user)
        member = HistoryMember.objects.filter(user=request.user).values_list("group__id","group__name").distinct()
        context = {'group':group,'member':member}
        return render(request,'home/group.html',context)
    else:
        return redirect('/login') 



def creategroup(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            group = Group.objects.filter(name=name)
            if len(group) == 1:
                messages.error(request,'Same Group Exists')
                return redirect('/create-group')
            else:
                group = Group(user=request.user,name=name)
                group.save()
                historymember = HistoryMember(user=request.user,group=group)
                historymember.save()
                messages.success(request,"Group Created")
                return redirect('/group')
        return render(request,'home/create-group.html')
    else:
        return redirect('/login') 

def groupdetails(request,id):
    if request.user.is_authenticated:
        try:
            try:
                group = Group.objects.get(user=request.user,id=id)
                # member = HistoryMember.objects.filter(user=request.user,group=group)
                member = HistoryMember.objects.filter(group=group)
                member_total = HistoryMember.objects.filter(group=group).values_list('user__id').distinct()
                total = len(member_total)
                # calculation
                member_filter = HistoryMember.objects.filter(group=group)
                data = member_filter.values('id','user__first_name','amount').values('user__first_name').distinct().annotate(
                running_amount=Window(
                    expression=Sum('amount'),
                    partition_by=[F('user__id')],                    
                ))

                
                context = {'group':group,'member':member,'total':total,'data':data}
                return render(request,'home/group-details.html',context)
            except:
                group = Group.objects.get(id=id)
                # member = HistoryMember.objects.filter(user=request.user,group=group)
                member = HistoryMember.objects.filter(group=group)

                member_total = HistoryMember.objects.filter(group=group).values_list('user__id').distinct()
                group.is_admin = False
                total = len(member_total)

                 # calculation
                member_filter = HistoryMember.objects.filter(group=group)

                data = member_filter.values('id','user__first_name','amount').values('user__first_name').distinct().annotate(
                running_amount=Window(
                    expression=Sum('amount'),
                    partition_by=[F('user__id')],                    
                ))

                
                context = {'group':group,'member':member,'total':total,'data':data}
                return render(request,'home/group-details.html',context)
        except:
            return redirect('/group')
    else:
        return redirect('/login')

def addmember(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            adduser = request.POST['adduser']
            user = User.objects.get(id=adduser)
            group = Group.objects.get(id=id)
            groupmember = HistoryMember(user=user,group=group)
            groupmember.save()
            return redirect('/group')
        try:
            group = Group.objects.get(user=request.user,id=id)
            if group.is_admin == True:
                user = User.objects.all()
                context = {'user':user,'group':group}
                return render(request,'home/add-member.html',context)
            else:
                messages.error(request,"Can't Add Member")
                return redirect('/group')
        except:
            return redirect('/group')

    else:
        return redirect('/login')


def sendmsg(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            group_id = request.POST['group']
            amount = request.POST['amount']
            desc = request.POST['desc']

            group = Group.objects.get(id=group_id)
            history_member = HistoryMember(user=user,group=group,amount=amount,desc=desc)
            history_member.save()
            return redirect(f'group/{group_id}')
        else:
            return redirect('/group')
    else:
        return redirect('/login')


def history(request):
    if request.user.is_authenticated:
        history = HistoryMember.objects.filter(user=request.user)[::-1]
        print(history)
        context = {'history':history}
        return render(request,'home/history.html',context)
    else:
        return redirect('/login')


def wallet(request):
     if request.user.is_authenticated:
        return render(request,'home/wallet.html')
     else:
            return redirect('/login')
