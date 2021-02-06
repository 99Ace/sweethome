from django.shortcuts import render, HttpResponse, redirect
from .forms import NewExpense
from .models import Expense

# Create your views here.
def index(request):
    results = Expense.objects.all()
    return render(request, 'index.html', {
        'details':results,
    })

def create(request):
    if request.method == "POST":
        new_entry_form = NewExpense(request.POST)
        if new_entry_form.is_valid():
            instance = new_entry_form.save(commit=False)
            instance.save()
        return redirect(index)
    else:
        new_entry_form = NewExpense()
        return render(request, 'new_expense.html',{
            'form': new_entry_form
            })
