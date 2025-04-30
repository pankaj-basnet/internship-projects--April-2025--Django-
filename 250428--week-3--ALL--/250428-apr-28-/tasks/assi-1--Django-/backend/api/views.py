from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

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

    # def perform_create(self, serializer): # sn= 
    #     # serializer.save(user=self.request.user)
    #     id = serializer.validated_data.get('id')
    #     print(id)
    #     # serializer.save(content=content)
    #     # send a Django signal



# class ProfilePage(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all() # gives all
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         print(self.request.user)

#         return self.request.user
    
# class ProfilePage(generics.ListAPIView):
#     '''
#     Not gonna use this method
#     '''
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

# # profile_list_view = ProfileListAPIView.as_view()
    

# =========================   
# class ProfilePage(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # lookup_field = 'pk' ??

# # product_detail_view = ProductDetailAPIView.as_view()
    
# =========================   
    
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.models import User
from .serializers import UserSerializer

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
        print(f"Retrieving profile for user: {user.username}")  # Optional debug print
        return user

# =========================   