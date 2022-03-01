from django.shortcuts import render, redirect

# Create your views here.
from library.my_app.forms import ProfileForm, BookForm
from library.my_app.models import Profile, Book

"""
http: // localhost: 8000 / - home page
http: // localhost: 8000 / add / - add book page
http: // localhost: 8000 / edit /:id - edit book page
http: // localhost: 8000 / details /:id - book details page
http: // localhost: 8000 / profile / - profile page
http: // localhost: 8000 / profile / edit / - edit profile page
http: // localhost: 8000 / profile / delete / - delete profile page
"""


def get_profile():
    have_a_profile = Profile.objects.all()
    if have_a_profile:
        have_a_profile = have_a_profile[0]
        return have_a_profile
    return None


def home(request):
    profile = get_profile()
    books = Book.objects.all()

    context = {
        'books': books,
        'profile': profile,
    }
    if profile:
        return render(request, 'home-with-profile.html', context)
    else:
        return render(request, 'home-no-profile.html')


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def add_book(request):
    profile = get_profile()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.profile = profile
            book.save()
            return redirect('home')
    else:
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book,
    }
    return render(request, 'book-details.html', context)


def profile_page(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    else:
        form = ProfileForm(instance=profile)
        context = {
            'form': form
        }
        return render(request, 'delete-profile.html', context)

