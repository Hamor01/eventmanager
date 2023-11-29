from django.db import models

# Create your models here.


class Event(models.Model):
    eventName = models.CharField(max_length=50, blank=False, null=False)
    # eventDescription = models.TextField(max_length=10000, blank=False, null=False)
    eventLocation = models.CharField(max_length=50, blank=False, null=False)
    # eventCapacity = models.PositiveIntegerField(blank=False, null=False)
    eventDate = models.DateField()
    # eventPoster = models.ImageField(upload_to="eventposters/", blank=False, null=False)
    # eventCost = models.PositiveIntegerField(blank=False, null=False)
    facebook = models.CharField(max_length=500, blank=True, null=True)
    twitter = models.CharField(max_length=500, blank=True, null=True)
    instagram = models.CharField(max_length=500, blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.eventName


# class Schedule(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     day = models.CharField(max_length=50)
#     time_start = models.TimeField()
#     time_end = models.TimeField()
#     artist = models.CharField(max_length=100)
#     background_color = models.CharField(max_length=7, default='#FFFFFF')
#     background_image = models.ImageField(upload_to='schedule/', blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.event.eventName} - {self.day} ({self.time_start} to {self.time_end})"


class Partner(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Award(models.Model):
    # heading = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Ticket(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    ticket_type = models.CharField(max_length=20, choices=[('early_bird', 'Early Bird'), ('standard', 'Standard')])
    num_tickets = models.PositiveIntegerField()
    description = models.TextField()

    def calculate_total_cost(self):
        if self.ticket_type == 'early_bird':
            return 5 * self.num_tickets
        elif self.ticket_type == 'standard':
            return 10 * self.num_tickets
        else:
            return 0  # Handle other ticket types if needed

    def __str__(self):
        return f"{self.name}'s Ticket"


class Schedule(models.Model):
    MorningHeading = models.CharField(max_length=200)
    # MorningTime = models.DateTimeField(auto_now=True)
    MorningAuthor = models.CharField(max_length=100)

    AfternoonHeading = models.CharField(max_length=200)
    # AfternoonTime = models.DateTimeField(auto_now=True)
    AfternoonAuthor = models.CharField(max_length=100)

    EveningHeading = models.CharField(max_length=200)
    # EveningTime = models.DateTimeField(auto_now=True)
    EveningAuthor = models.CharField(max_length=100)


def __str__(self):
        return self.Morningheading


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name



