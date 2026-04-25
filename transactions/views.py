from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages

# Create your views here.

@login_required
def transaction_list(request):

    #Get the search query from the URL
    search_query = request.GET.get('search', '')
    category_query = request.GET.get('category', '')

    #This will fetch all transactions from the database
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    #Apply filters if they exist
    if search_query:
        transactions = transactions.filter(title__icontains=search_query)

    if category_query:
        transactions = transactions.filter(category__icontains=category_query)

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

@login_required
def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    
    return render(request, 'transactions/transaction_form.html', {
        'form': form, 
        'edit_mode': True
    })
    

@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        transaction.delete()
        messages.success(request, "Transaction deleted successfully!")
        return redirect('transaction_list')
    return render(request, 'transactions/transaction_confirm_delete.html', {'transaction': transaction})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('transaction_list')
        else:
            form = UserCreationForm()
        return render(request, 'transactions/register.html', {'form': form})