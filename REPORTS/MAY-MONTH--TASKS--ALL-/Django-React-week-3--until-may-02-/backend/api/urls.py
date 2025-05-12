# =============================
# D:\GROW_CTS\PANKAJ-PROJECTS-\REPORTS\MAY-MONTH--TASKS--ALL-\Django-React-week-3--until-may-02-\backend\api\urls.py
# =============================


from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


#
from .views import ManualPasswordResetView


# from . import blog

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    
    path("blog/", include("blog.urls")),

 
    path('profile/', views.ProfilePage.as_view(), name='profile'),

 

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html",
        email_template_name="registration/password_reset_email.txt",
        html_email_template_name="registration/password_reset_email.html",
        subject_template_name="registration/password_reset_subject.txt",
    ), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html"
    ), name='password_reset_done'),
 
    # 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html"
    ), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"
    ), name='password_reset_complete'),

    # 
    path("manual_reset_email/", ManualPasswordResetView.as_view(), name="manual_reset_email"),

]
