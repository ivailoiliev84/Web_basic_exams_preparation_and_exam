from django.urls import path

from expenses_tracker.main_app.views import *

"""urlpatterns = (

    path('', home_page, name='home page'),
    path('create/', create_expense_page, name='create expense page'),
    path('edit/<int:pk>', edit_expense_page, name='edit expense page'),
    path('delete<int:pk>', delete_expense_page, name='delete expense page'),



    path('profile/', profile_page, name='profile page'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', profile_edit_page, name='profile page'),
    path('profile/delete/', delete_profile_page, name='profile edit page'),

)"""

urlpatterns = (
    path('', home_page, name='home page'),
    path('create/', create_expense_page, name='create expense page'),
    path('edit/<int:pk>', edit_expense_page, name='edit expense page'),
    path('delete/<int:pk>', delete_expense_page, name='delete expense page'),

    path('profile/', profile_page, name='profile page'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', profile_edit_page, name='edit profile'),
    path('profile/delete/', delete_profile_page, name='delete profile'),

)
