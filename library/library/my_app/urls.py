from django.urls import path

from library.my_app.views import *

"""
http: // localhost: 8000 / - home page
http: // localhost: 8000 / add / - add book page
http: // localhost: 8000 / edit /:id - edit book page
http: // localhost: 8000 / details /:id - book details page
http: // localhost: 8000 / profile / - profile page
http: // localhost: 8000 / profile / edit / - edit profile page
http: // localhost: 8000 / profile / delete / - delete profile page
"""


urlpatterns = (
    path('', home, name='home'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('details/<int:pk>', details_book, name='details book'),
    path('profile/', profile_page, name='profile page'),
    path('create-profile/', create_profile, name='create profile'),
    path('edit-profile/', edit_profile, name='edit profile'),
    path('delete-profile/', delete_profile, name='delete profile')
)