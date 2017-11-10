from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
    user_firstname = models.CharField(max_length=40)
    user_lastname = models.CharField(max_length=40)
    user_phone = models.CharField(max_length=40)
    user_email = models.CharField(max_length=100)


    def get_absolute_url(self):
        return reverse('appointmenthome:info',kwargs={'pk': self.pk})

    def __str__(self):
        return self.user_firstname + ' ' + self.user_lastname

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    notes = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.location + ' ' + self.date
