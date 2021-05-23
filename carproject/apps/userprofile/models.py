from django.contrib.auth.models import User
from django.db import models

from apps.car.models import Dealership


class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)


User.userprofile = property(lambda u: Userprofile.objects.get_or_create(user=u)[0])


class ConversationMessage(models.Model):
    dealership = models.ForeignKey(Dealership, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete=models.CASCADE)
