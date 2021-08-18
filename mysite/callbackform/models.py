from django.db import models
import datetime
# Create your models here.

class CallbackForm(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40,blank=True)
    company = models.CharField(max_length=80,blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=240)
    problem_description = models.CharField(max_length=2000)
    comment = models.CharField(max_length=2000,blank=True)
    archive = models.BooleanField(default=False)
    support_datetime = models.DateTimeField(default=datetime.datetime.now)
    create_date = models.DateTimeField(auto_now_add=True)

    # Return name of the record with subject text
    def __str__(self):
        return self.subject
