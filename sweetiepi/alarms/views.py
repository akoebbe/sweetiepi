from datetime import datetime, time

from django.http import HttpResponse

from .models import RecurringAlarm

# Create your views here.


def index(request):
    alarms = RecurringAlarm.objects.order_by('-id')
    last_check = datetime(2014, 03, 27, 6, 00, 00)
    now = datetime(2014, 03, 28, 7, 00, 01)
    output = ''
    for alarm in alarms:
        occurrences = list(alarm.recurrences.between(
            after=last_check,
            before=now,
            inc=True,
            dtstart=datetime.combine(last_check.date(), time(0, 0)),
        ))
        for occurrence in occurrences:
            if last_check < datetime.combine(occurrence.date(), alarm.time) < now:
                output = "Alarm - ", alarm
    return HttpResponse(output)