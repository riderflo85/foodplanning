from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .callr import api


@shared_task
def send_notification(num, msg):
    """ Added task to the queue """

    result = api.call('sms.send', 'SMS', num, msg, None)

    return result
