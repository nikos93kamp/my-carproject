from django.contrib.auth.models import User
from django.db import models

class Notification(models.Model):
    MESSAGE = 'message'
    DEALERSHIP = 'dealership'

    CHOICES = (
        (MESSAGE, 'Message'),
        (DEALERSHIP, 'Dealership')
    )

    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)

    created_by = models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE)
