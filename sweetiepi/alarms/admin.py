from __future__ import absolute_import

from django.contrib import admin

from .models import RecurringAlarm, SingleAlarm


admin.site.register([RecurringAlarm, SingleAlarm])