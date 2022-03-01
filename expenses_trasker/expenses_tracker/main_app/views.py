from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker.main_app.forms import ProfileCreateForm, ExpenseForm
from expenses_tracker.main_app.models import Profile, Expense


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    form = ProfileCreateForm()

    context = {
        'profile': profile,
        'expenses': expenses,
        'form': form,

    }
    if profile:
        return render(request, 'home-with-profile.html', context)
    else:
        return render(request, 'home-no-profile.html', context)


def create_profile(request):
    if request.method == "POST":
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:

        form = ProfileCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def create_expense_page(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ExpenseForm()
    context = {
        'form': form
    }
    return render(request, 'expense-create.html', context)


def edit_expense_page(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ExpenseForm(instance=expense)
    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense_page(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense.delete()
            return redirect('home page')
    else:
        form = ExpenseForm(instance=expense)
        context = {
            "form": form,
            'expense': expense,
        }
        return render(request, 'expense-delete.html', context)


def profile_page(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    left_money = profile.budget - sum(expense.price for expense in expenses)

    context = {
        'profile': profile,
        'number_of_expenses': len(expenses),
        'left_money': f"{left_money:.2f}",
    }
    return render(request, 'profile.html', context)


def profile_edit_page(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileCreateForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile_page(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        return redirect('home page')

