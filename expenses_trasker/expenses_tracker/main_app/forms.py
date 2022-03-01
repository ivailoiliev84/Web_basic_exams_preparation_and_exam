from django import forms

from expenses_tracker.main_app.models import Profile, Expense


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image',)
        widgets = {
            'profile_image': forms.FileInput(attrs={'class': "form-file"})
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price',)
