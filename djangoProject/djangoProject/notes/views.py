from django.shortcuts import render, redirect

# Create your views here.
from djangoProject.notes.forms import ProfileForm, NoteForm
from djangoProject.notes.models import Profile, Note

"""
• http: // localhost: 8000 / - home
page
• http: // localhost: 8000 / add - add
note
page
• http: // localhost: 8000 / edit /:id - edit
note
page
• http: // localhost: 8000 / delete /:id - delete
note
page
• http: // localhost: 8000 / details /:id - note
details
page
• http: // localhost: 8000 / profile - profile
page
"""


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]

    return None


def home(request):
    profile = get_profile()
    form = ProfileForm
    notes = Note.objects.all()

    context = {
        'profile': profile,
        'form': form,
        'notes': notes
    }
    if profile == None:
        return render(request, 'home-no-profile.html', context)
    else:
        return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form

    }
    return render(request, 'home-no-profile.html', context)


def add_note(request):
    profile = get_profile()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.profile = profile
            note.save()
            return redirect('home')
    else:
        form = NoteForm()
    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('home')
    else:
        form = NoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def profile_page(request):
    profile = get_profile()
    all_notes = profile.note_set.count()

    context = {
        'profile': profile,
        'all_notes': all_notes,

    }
    return render(request, 'profile.html', context)


def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('home')
    else:
        context = {
            'profile': profile
        }
        return render(request, 'profile-delete.html', context)
