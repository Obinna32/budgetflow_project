from django.shortcuts import render
from .models import Transaction

# Create your views here.
def transaction_list(request):
    #This will fetch all transactions from the database
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'transactions/index.html', {
        'transactions': transactions
    })