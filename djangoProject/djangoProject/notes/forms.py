from django import forms

from djangoProject.notes.models import Profile, Note


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('profile',)
