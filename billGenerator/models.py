from django.db import models

# Create your models here.
import datetime
import uuid
from django.utils import timezone

class Account(models.Model):
    #account owner
    owner = models.CharField(max_length=30)
    iban = models.CharField(max_length=22)
    bic = models.CharField(max_length=11)

    def __str__(self):
        return "Account of " + self.owner



class Course(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    employee = models.ForeignKey('Trainer', blank=True, null=True)
    customers = models.ForeignKey('Customer', blank=True, null=True)
    autoBill = models.BooleanField('Shall this course be auto-billed?')
    beginTime = models.TimeField('Starting time of the course')
    endTime = models.TimeField('End time of the course')
    beginDate = models.DateField('Start date of the course')
    endDate = models.DateField('End date of the course')
    dayOfWeek = models.CharField(max_length=10)

    #nextSession = models.DateTimeField(name='next session')

    def next_session(self):
        now = timezone.now()
        if now - self.EndDate > 0:
            return self.EndDate
        else:
            for next in range((self.EndDate -self.beginDate).days):
                if now - next <0:
                    return next


    next_session.admin_order_field = 'nextSession'
    next_session.short_description = 'next session'

    def __str__(self):
        return self.title

    def length(self):
        return self.endTime - self.beginTime

class Customer(models.Model):
    name = models.CharField(max_length=30)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    courses = models.ForeignKey('Course', blank=True, null=True)
    SEPAvalid = models.BooleanField('Is the SEPA valid?')
    addressStreet = models.CharField(max_length=30, name='street', default='Franz-Liszt-Straße')
    addressHouseNr = models.IntegerField(name='house number', default=34)
    addressHouseNrExtra = models.CharField(max_length=1,name='extra to the house number', blank=True)
    addressPostalCode = models.IntegerField(name='postal code', default=38106)
    addressCity = models.CharField( max_length=20, name='city', default='Braunschweig')
    account = models.ForeignKey('Account', name='Account which pays for courses')

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=30)
    addressStreet = models.CharField(max_length=30, name ='street', default='Franz-Liszt-Straße')
    addressHouseNr = models.IntegerField(name='house number', default=34)
    addressHouseNrExtra = models.CharField(max_length=1, name='extra to the house number', blank=True)
    addressPostalCode = models.IntegerField(name='postal code', default=38106)
    addressCity = models.CharField(name='city', max_length=20, default='Braunschweig')
   #account data of trainer
    accountInfo = models.ForeignKey('Account', name='Account to pay to')
   #courses the trainer gives
    courses = models.ForeignKey('Course', name='Courses given by trainer', blank=True, null=True)#models.UUID
    dateFirstAid = models.DateField('latest first aid certificate')




    def __str__(self):
        return "Trainer " + self.name