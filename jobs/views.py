from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from .county import counties
from . models import Job, Bid
from . forms import AddJobForm, BidForm
from django.core.mail import send_mail


def home_view(request):
    context = {}
    context['jobs'] = Job.objects.filter(status="pending")
    return render(request, 'jobs/home.html', context)


@login_required(login_url='login_view')
def admin_dashboard(request):
    context = {}
    context['members'] = Account.objects.all()
    context['total_bids'] = Bid.objects.all().count()
    context['total_technician'] = Account.objects.filter(role="technician").count()
    context['total_clients'] = Account.objects.filter(role="client").count()
    return render(request, 'jobs/adminHome.html', context)


@login_required(login_url='login_view')
def client_dashboard(request):
    context = {}
    context['counties'] = counties
    context['email'] = request.user.email
    context['phone'] = request.user.phoneNumber
    context['name'] = request.user.fullName
    context['jobs'] = Job.objects.filter(created_by=request.user.id)
    return render(request, 'jobs/clientHome.html', context)


@login_required(login_url='login_view')
def technician_dashboard(request):
    context = {}
    context['jobs'] = Job.objects.filter(status="pending")
    return render(request, 'jobs/technicianHome.html', context)


@login_required(login_url='login_view')
def addjob(request):
    if request.POST:
        data = request.POST
        data._mutable = True
        data['created_by'] = request.user
        form = AddJobForm(data)
        if form.is_valid():
            form.save()
            return redirect('client_dashboard')
        else:
            print(form.errors)
    return redirect('client_dashboard')


def more_info_view(request, id):
    context = {}
    job = Job.objects.get(id=id)
    context['job'] = job
    context['total_bids'] = Bid.objects.filter(job=id).count()
    context['bids'] = Bid.objects.filter(job=id)
    return render(request, 'jobs/MoreInfo.html', context)


@login_required(login_url='login_view')
def bidd(request, id):
    if request.POST:
        data = {}
        data['technician'] = request.user
        data['job'] = id
        data['amount'] = request.POST.get('amount')
        form = BidForm(data)
        if form.is_valid():
            form.save()
            return redirect("technician_dashboard")
        else:
            print(form.errors)
    return redirect("technician_dashboard")


@login_required(login_url='login_view')
def get_all_technicians(request):
    context = {}
    technicians = Account.objects.filter(role="technician")
    context['technicians'] = technicians
    return render(request, 'jobs/alltechnicians.html', context)


@login_required(login_url='login_view')
def get_all_clients(request):
    context = {}
    clients = Account.objects.filter(role="client")
    context['clients'] = clients
    return render(request, 'jobs/allClients.html', context)


@login_required(login_url='login_view')
def assign_job(request, id, job_id):
    context = {}
    data = {}
    plumber = Account.objects.get(id=id)    
    data['technician'] = id
    data['job'] = job_id
    job = Job.objects.get(id=job_id)
    message = 'Bid assigned successfully for {}'.format(job.title)
    send_mail('Bid Assignment', message, 'sender email',
              ['to technician email'], fail_silently=False)
    return redirect('client_dashboard')

@login_required(login_url='login_view')
def close_job(request,id):
    Job.objects.filter(id=id).update(status='completed')
    return redirect('client_dashboard')
