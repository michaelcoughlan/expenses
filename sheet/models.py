from django.db import models

# Create your models here.
class Row(models.Model):
    income = models.IntegerField()
    expenditure = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Amount: {}, Date: {}".format((self.income - self.expenditure), self.created_at)
