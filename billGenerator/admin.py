from django.contrib import admin
# Register your models here.
from .models import Course, Customer, Account, Trainer

admin.site.register(Course)
admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Trainer)