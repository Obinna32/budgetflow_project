from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        #We want the user to fill only these fields
        fields = ['title', 'amount', 'category', 'transaction_type', 'date']
        #This adds a calendar pickr to th date field
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }