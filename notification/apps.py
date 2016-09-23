from __future__ import unicode_literals

from django.apps import AppConfig


class NotificationConfig(AppConfig):
    name = 'notification'


    def ready(self):
        import notification.signals.handlers

# for further reading : Build Quora count function with Django Signals
