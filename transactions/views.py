from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def transaction_list(request):
    #This will fetch all transactions from the database
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'transactions/index.html', {
        'transactions': transactions
    })

@login_required
def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user #This assigns the current logged-in user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/transaction_form.html', {'form':form})