from __future__ import absolute_import

from django.db import models

from clocks import choices


class ClockStyle(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=0)
    dial = models.CharField(max_length=100, choices=choices.DIAL_CHOICES, default='din 41091.4')
    hourHand = models.CharField(max_length=100, choices=choices.HOUR_HAND_CHOICES, default='din 41092.3')
    minuteHand = models.CharField(max_length=100, choices=choices.MINUTE_HAND_CHOICES, default='din 41092.3')
    secondHand = models.CharField(max_length=100, choices=choices.SECOND_HAND_CHOICES, default='din 41071.1')
    minuteHandBehavior = models.CharField(max_length=100, choices=choices.MINUTE_HAND_MOVEMENT_CHOICES, default='sweeping')
    secondHandBehavior = models.CharField(max_length=100, choices=choices.SECOND_HAND_MOVEMENT_CHOICES, default='stepping')
    secondHandStopToGo = models.BooleanField(default=False)
    secondHandStopTime = models.FloatField(default=0)
    backgroundColor = models.CharField(max_length=20, default='0,0,0,1')
    dialColor = models.CharField(max_length=11, default='255,255,255')
    hourHandColor = models.CharField(max_length=11, default='0,0,0')
    minuteHandColor = models.CharField(max_length=11, default='0,0,0')
    secondHandColor = models.CharField(max_length=11, default='0,0,0')
    axisCoverColor = models.CharField(max_length=11, default='0,0,0')
    axisCoverRadius = models.PositiveIntegerField(default=7)
    updateInterval = models.PositiveIntegerField(default=50)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.active:
            ClockStyle.objects.filter(active=True).update(active=False)
        super(ClockStyle, self).save(*args,**kwargs)