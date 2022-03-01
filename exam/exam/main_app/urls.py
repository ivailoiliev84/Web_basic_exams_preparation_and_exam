from django.urls import path

from exam.main_app.views import *

"""
    • http://localhost:8000/ - home page
    • http://localhost:8000/album/add/ - add album page
    • http://localhost:8000/album/details/<id>/ - album details page
    • http://localhost:8000/album/edit/<id>/ - edit album page
    • http://localhost:8000/album/delete/<id>/ - delete album page
    • http://localhost:8000/profile/details/ - profile details page
    • http://localhost:8000/profile/delete/ - delete profile page
"""
urlpatterns = (
    path('', home_page, name='home page'),
    path('album/add/', create_album, name='create album'),
    path('album/details/<int:pk>', details_album, name='details album'),
    path('album/edit/<int:pk>',edit_album, name='edit album'),
    path('album/delete/<int:pk>', delete_album, name='delete album'),

    path('create/profile/', create_profile, name='profile create'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='profile delete'),
)
