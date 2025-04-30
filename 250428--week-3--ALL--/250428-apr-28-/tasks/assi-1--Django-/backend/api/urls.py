from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    
    # w03d01t01 sn=
    # path('profile/<int:pk/', views.ProfilePage.as_view(), name='profile'),
    path('profile/', views.ProfilePage.as_view(), name='profile'),

    # other URLs
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
]
