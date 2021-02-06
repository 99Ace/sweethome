from django import forms
from .models import Expense

class NewExpense(forms.ModelForm):
    class Meta:
        model = Expense        
        fields = (
            'name',
            'price',
            'vendor',
            'category'
        )