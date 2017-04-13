from django.db import models

# Create your models here.
import datetime
import uuid




class Account(models.Model):
    #account owner
    owner = models.CharField(max_length=30)
    iban = models.CharField(max_length=22)
    bic = models.CharField(max_length=11)

    def __str__(self):
        return "Account of " + self.owner



class Course(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20,name='Course title')
    trainer = models.ForeignKey('Trainer')
    customers = models.ForeignKey('Customer')
    autoBill = models.BooleanField('Shall this course be auto-billed?')
    beginTime = models.DateTimeField('Starting time of the course')
    endTime = models.DateTimeField('End time of the course')
    beginDate = models.DateField('Start date of the course')
    endDate = models.DateField('End date of the course')

    def __str__(self):
        return self.title

    def length(self):
        return self.endTime - self.beginTime

class Customer(models.Model):
    name = models.CharField(max_length=30, name='Customer name')
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    courses = models.ForeignKey('Course', name='Courses visited by customer')
    SEPAvalid = models.BooleanField('Is the SEPA valid?')
    address = models.CharField(max_length=30)
    account = models.ForeignKey('Account', name='Account which pays for courses')

    def __str__(self):
        return self.name


class Trainer(Customer):
   #account data of trainer
    accountInfo = models.ForeignKey('Account', name='Account to pay to')
   #courses the trainer gives
    courses = models.ForeignKey('Course', name='Courses given by trainer')#models.UUID
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dateFirstAid = models.DateField('latest first aid certificate')


    def __str__(self):
        return "Trainer " + self.name