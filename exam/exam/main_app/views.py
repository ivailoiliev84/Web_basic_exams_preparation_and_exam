from django.shortcuts import render, redirect

# Create your views here.
from exam.main_app.forms import ProfileForm, AlbumForm
from exam.main_app.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    albums = Album.objects.all()
    form = ProfileForm()

    context = {
        'profile': profile,
        'albums': albums,
        'form': form,
    }
    if profile:
        return render(request, 'home-with-profile.html', context)
    else:
        return render(request, 'home-no-profile.html', context)


def create_album(request):
    profile = get_profile()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = AlbumForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
        'profile': profile
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    profile = get_profile()
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = AlbumForm(instance=album)
    context = {
        'form': form,
        'profile': profile,
        'album': album,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('home page')

    else:
        form = AlbumForm(instance=album)
    context = {
        'form': form,
        'profile': profile,
        'album': album,
    }
    return render(request, 'delete-album.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    number_of_albums = Album.objects.all()

    context = {
        'profile': profile,
        'number_of_albums': len(number_of_albums)
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        return redirect('home page')
    else:
        return render(request, 'profile-delete.html')
