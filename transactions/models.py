from django.db import models, migrations
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('expense', 'Expense'),
        ('income', 'Income'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"