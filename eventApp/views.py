from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Event, Partner, Schedule, Award, Contact
from django.contrib import messages
from .forms import TicketForm



# Create your views here.


def index(request):

    schedules = Schedule.objects.all()

    context = {'schedules': schedules}

    event = Event.objects.order_by('-eventDate').first()

    context = {"event": event}

    return render(request, 'index.html', context)


def ticket(request):
    context = {'ticket': ticket}
    return render(request, 'ticket.html', context)


def partner(request):

    partner = Partner.objects.all()

    context = {'partner': partner}

    return render(request, 'partner.html', context)



def award(request):
    award = Award.objects.first()
    return render(request, 'award.html', {'award': award})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')  # Updated to match the form field name
        company = request.POST.get('company')  # Updated to match the form field name
        message = request.POST.get('message')  # Updated to match the form field name

        contact = Contact(name=name, email=email, company=company, message=message)
        contact.save()

        

    return render(request, 'contact.html')


def schedule(request):
    schedule = Schedule.objects.all()
    context = {'schedule': schedule}
    return render(request, 'schedule.html', context)


def pricing(request):
    context = {'pricing': pricing}
    return render(request, 'pricing.html', context)


def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_instance = form.save()
            total_cost = ticket_instance.calculate_total_cost()
            messages.success(request, f"Payment successful! Total cost: Ksh. {total_cost}")
            return redirect(request, 'eventApp:ticket')  # Assuming 'ticket' is the URL name for the ticket view
    else:
        form = TicketForm()

    return render(request, 'ticket.html', {'form': form})


