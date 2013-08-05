from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms

import newcalendar

import datetime
from models import Event

class eventform(forms.Form):
    date = forms.DateField()
    description = forms.CharField(max_length=100)

class CalendarVarOne(newcalendar.LinkyCalendar):
    monthclass = "monthvar1"
    cssclasses = ['yes', 'yes', 'no', 'no','no', 'yes', 'no']
    navlinkstext = ['-', '+']

class CalendarVarTwo(newcalendar.LinkyCalendar):
    monthclass = "monthvar2"
    cssclasses = ['no', 'no', 'yes', 'yes', 'yes', 'yes', 'no']
    navlinkstext = ['prev','next']

def default(request):
    today = datetime.datetime.today()
    return index(request, today.year, today.month)

def index(request, year, month):
    month = int(month)
    year = int(year)
    calendar = newcalendar.LinkyCalendar()
    calendar1 = CalendarVarOne()
    calendar2 = CalendarVarTwo()
    if request.method == "POST":
        form = eventform(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            ev = Event(date=date, description=description)
            ev.save()
    data = {}

    for event in Event.objects.all():
        if event.date.year == year and \
           event.date.month == month:
                data[event.date.day] = fix_date(event.date.day)

    form = eventform() 
    firstmonth = calendar.formatmonth(year, month, data=data)
    secondmonth = calendar1.formatmonth(year, month, data=data)
    thirdmonth = calendar2.formatmonth(year, month, data=data)
    return render_to_response('index.html', {"calendar1":unicode(firstmonth),
                                             "calendar2":unicode(secondmonth),
                                             "calendar3":unicode(thirdmonth),
                                             "form":form,
                                            },
                              context_instance=RequestContext(request),
                             )

def day(request, year, month, day):
    events = []
    for event in Event.objects.all():
        if event.date.year == int(year) and \
           event.date.month == int(month) and \
           event.date.day == int(day):
            print event
            events.append(event)
    return render_to_response('events.html', {'date': "{0}/{1}/{2}".format(year, month, day),
                                              'events':events})

def fix_date(month):
    if month < 10:
        month = "0" + str(month)
    return month
