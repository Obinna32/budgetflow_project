from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.

@login_required
def transaction_list(request):
    #This will fetch all transactions from the database
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    #Calculate Total income
    total_income = transactions.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0

    #Calculate Total Expense
    total_expense = transactions.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    #Calculate Net Balance
    balance = total_income - total_expense

    context = {
        'transactions' : transactions,
        'total_income' : total_income,
        'total_expense': total_expense,
        'balance': balance,
    }

    return render(request, 'transactions/index.html', context)

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