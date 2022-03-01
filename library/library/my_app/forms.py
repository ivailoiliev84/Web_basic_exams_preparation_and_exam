from django import forms

from library.my_app.models import Profile, Book


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('profile',)
