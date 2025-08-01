from django.db import models

class Transaction(models.Model):
    product_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    transaction_date = models.DateField()

    def total_price(self):
        return self.amount * self.quantity

    def __str__(self):
        return f"{self.product_name} - {self.transaction_date}"
