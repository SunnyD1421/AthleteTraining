from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import ThrowingSchedule, Athlete, ThrowPlans, Throwing
from .forms import ThrowingForm, ThrowDescForm, ThrowScheduleForm, ThrowPlanForm, LiftDescForm, LiftScheduleForm, LiftPlanForm, UserCreateForm
import datetime

def home(request):
    context = {
        'title':'Training Home'
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    elif request.user.groups.filter(name='Athlete').exists():
        return redirect('/athlete-dashboard')
    elif request.user.groups.filter(name='Coach').exists():
        return redirect('/coach-dashboard')
    else:
        return render(request, 'training/home.html', context)

def signup(request):
    context = {
        'title':'Signup'
    }
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get("password2")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreateForm()
    context['form'] = form
    return render(request, 'training/signup.html', context)

def about(request):
    context = {
        'title':'About'
    }
    return render(request, 'training/about.html', context)

def scheduleAth(request, year, month, day):
    d = datetime.date(year,month,day)
    throwing = Throwing(ath_user=request.user, throw_date=d)
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    elif not request.user.groups.filter(name='Athlete').exists():
        return redirect('/')
    elif ThrowingSchedule.objects.filter(ath_user_id = request.user.id, date = d).first()==None:
        return render(request, 'training/scheduleAth.html', {'athlete': request.user})
    else:
        throwSchedule = ThrowingSchedule.objects.get(ath_user_id = request.user.id, date = d)
        plan = ThrowPlans.objects.get(plan_name = throwSchedule.plan)
        context = {
            'throw_data': Throwing.objects.filter(ath_user_id=request.user.id, throw_date=d),
            'date': datetime.date(year,month,day),
            'year': year,
            'month': month,
            'day': day,
            'athlete': request.user,
            'throwSchedule': throwSchedule, 
            'plan': plan,
    }
    if request.method == 'POST':
        d = datetime.date(year,month,day)
        form = ThrowingForm(request.POST, instance=throwing)
        if form.is_valid():
            form.save()
            return redirect("/athlete-dashboard/"+str(year)+"/"+str(month)+"/"+str(day))
    else:
        form = ThrowingForm(instance=throwing)
    context['form'] = form
    return render(request, 'training/scheduleAth.html', context)

def visualize(request):
    context = {
        ## edit ##
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    else:
        return render(request, 'training/visualize.html', context)

def visualizeThrow(request):
    context = {
        ## edit ##
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    else:
        return render(request, 'training/visualizeThrow.html', context)

def visualizeLift(request):
    context = {
        ## edit ##
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    else:
        return render(request, 'training/visualizeLift.html', context)

def athDash(request):
    context = {
        'athlete': request.user,

    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    elif request.user.groups.filter(name='Coach'):
        return redirect('/coach-dashboard')
    else:
        return render(request, 'training/baseAthlete.html', context)

def coachDash(request):
    context = {
        ## edit ##
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    elif request.user.groups.filter(name='Athlete'):
        return redirect('/athlete-dashboard')
    else:
        return render(request, 'training/dashCoach.html', context)

def editThrowdesc(request):
    context = {
        ## edit ##
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    elif request.user.groups.filter(name='Athlete'):
        return redirect('/athlete-dashboard')
    elif request.method == 'POST':
        form = ThrowDescForm(request.POST)
        if form.is_valid():
            
            form.save()
    else:
        form =ThrowDescForm()

    context['form'] = form
    return render(request, 'training/editThrowDesc.html', context)

def editThrowschedule(request):
    context = {
        ## edit ##
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    elif request.user.groups.filter(name='Athlete'):
        return redirect('/athlete-dashboard')
    elif request.method == 'POST':
        form = ThrowScheduleForm(request.POST)
        if form.is_valid():
            
            form.save()
    else:
        form =ThrowScheduleForm()

    context['form'] = form
    return render(request, 'training/editThrowSchedule.html', context)

def editThrowplan(request):
    context = {
        ## edit ##
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    elif request.user.groups.filter(name='Athlete'):
        return redirect('/athlete-dashboard')
    elif request.method == 'POST':
        form = ThrowPlanForm(request.POST)
        if form.is_valid():
            
            form.save()
    else:
        form =ThrowPlanForm()

    context['form'] = form
    return render(request, 'training/editThrowPlans.html', context)

def editLiftdesc(request):
    context = {
        ## edit ##
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    elif request.user.groups.filter(name='Athlete'):
        return redirect('/athlete-dashboard')
    elif request.method == 'POST':
        form = LiftDescForm(request.POST)
        if form.is_valid():
            
            form.save()
    else:
        form =LiftDescForm()

    context['form'] = form
    return render(request, 'training/editLiftDesc.html', context)

def editLiftschedule(request):
    context = {
        ## edit ##
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    elif request.user.groups.filter(name='Athlete'):
        return redirect('/athlete-dashboard')
    elif request.method == 'POST':
        form = LiftScheduleForm(request.POST)
        if form.is_valid():
            
            form.save()
    else:
        form =LiftScheduleForm()

    context['form'] = form
    return render(request, 'training/editLiftSchedule.html', context)

def editLiftplan(request):
    context = {
        ## edit ##
    }
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    elif request.user.groups.filter(name='Athlete'):
        return redirect('/athlete-dashboard')
    elif request.method == 'POST':
        form = LiftPlanForm(request.POST)
        if form.is_valid():
            
            form.save()
    else:
        form =LiftPlanForm()

    context['form'] = form
    return render(request, 'training/editLiftPlans.html', context)