from django.db import models
from datetime import datetime

# Create your models here.
class Row(models.Model):
    income = models.IntegerField()
    expenditure = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    readonlyfields = ['created_at', 'updated_at']

    def __str__(self):
        return "Amount: {} ({})".format((self.income - self.expenditure), self.created_at.strftime('%d-%m-%Y'))
