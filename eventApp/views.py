from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Event, Partner, Schedule, Award, Contact, Ticket
from django.contrib import messages
from .forms import TicketForm



# Create your views here.


def index(request):

    schedules = Schedule.objects.all()

    context = {'schedules': schedules}

    event = Event.objects.order_by('-eventDate').first()

    context = {"event": event}

    return render(request, 'index.html', context)


# def ticket(request):
#     ticket = Ticket.objects.all()
#     context = {'ticket': ticket}
#     return render(request, 'ticket.html', context)



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


# def ticket(request):
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             ticket_instance = form.save()
#             total_cost = ticket_instance.calculate_total_cost()
#             messages.success(request, f"Payment successful! Total cost: Ksh. {total_cost}")
#             return redirect(request, 'eventApp:ticket')  # Assuming 'ticket' is the URL name for the ticket view
#     else:
#         form = TicketForm()
#
#     return render(request, 'ticket.html', {'form': form})


def ticket(request):
    if request.method == 'POST':
        # Process form data and save to the database
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        ticket_type = request.POST.get('ticket_type')
        num_tickets = request.POST.get('num_tickets')
        description = request.POST.get('description')

        if not ticket_type:
            messages.error(request, 'Please select a ticket type.')
            return render(request, 'ticket.html')

        ticket = Ticket.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            ticket_type=ticket_type,
            num_tickets=num_tickets,
            description=description
        )
        ticket.save()
        return render(request, 'success.html')

    return render(request, 'ticket.html')


def success(request):
    return render(request, 'success.html')