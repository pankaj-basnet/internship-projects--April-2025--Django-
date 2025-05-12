# ============================
# D:\GROW_CTS\PANKAJ-PROJECTS-\REPORTS\MAY-MONTH--TASKS--ALL-\Django-React-week-3--until-may-02-\backend\api\views.py
# ============================

from django.shortcuts import render

# from django.contrib.auth.models import User
from api.models import User

from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication

# from django.contrib.auth.models import User
from .models import User

from .serializers import UserSerializer

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    # permission_classes = [IsAdminUser, IsAuthenticated]
    permission_classes = [ IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

 

class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        # if not instance.content:
        #     instance.content = instance.title
            ## 

profile_update_view = ProfileUpdateAPIView.as_view()

    

class ProfilePage(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()  # Required by DRF for generic views, even if overridden
    serializer_class = UserSerializer
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


    def get_object(self):
        """
        This method ensures that only the authenticated user's
        own profile is retrieved and updated.
        """
        user = self.request.user  # Get the current logged-in user
        # print(f"Retrieving profile for user: {user.get_email_field_name}")  # Optional debug print
        return user
    
                




# =========================   
# =========================   


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views import View

User = get_user_model()

@method_decorator(csrf_protect, name='dispatch')
class ManualPasswordResetView(View):
    def get(self, request):
        return render(request, "password_reset_form_custom.html")

    def post(self, request):
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, "password_reset_form_custom.html", {
                "error": "No user found with that email."
            })

        # Token and UID generation
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        domain = get_current_site(request).domain
        protocol = "https" if request.is_secure() else "http"

        context = {
            "user": user,
            "uid": uid,
            "token": token,
            "domain": domain,
            "protocol": protocol,
        }

        # Render email
        text_content = render_to_string("emails/password_reset_email.txt", context)
        html_content = render_to_string("emails/password_reset_email.html", context)

        subject = "Reset Your Password"
        from_email = "pankajbasnet2023@example.com"
        to_email = [user.email]

        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return render(request, "password_reset_form_custom.html", {
            "success": "Password reset email has been sent."
        })


# =========================   
# =========================   