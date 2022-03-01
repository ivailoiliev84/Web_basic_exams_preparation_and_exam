from django.urls import path


from .views import *



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

urlpatterns = (
    path('', home, name='home'),
    path('create/', create_profile, name='create profile'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete'),
    path('details/<int:pk>', details_note, name='details note'),
    path('profile/', profile_page, name='profile page'),
    path('delete-profile/<int:pk>', delete_profile, name='delete profile'),

)
