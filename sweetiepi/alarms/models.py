from django.db import models
import recurrence.fields


class RecurringAlarm(models.Model):
    name = models.CharField(max_length=255)
    time = models.TimeField()
    recurrences = recurrence.fields.RecurrenceField()

    def __unicode__(self):
        return self.name


class SingleAlarm(models.Model):
    name = models.CharField(max_length=255)
    datetime = models.DateTimeField()

    def __unicode__(self):
        return self.name
