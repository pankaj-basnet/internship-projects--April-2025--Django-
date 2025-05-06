# D:\GROW_CTS\Django-React-Full-Stack-App-main\backend\blog\views.py

from rest_framework import generics, permissions, mixins, authentication
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Post, Comment  
from .serializers import PostSerializer, CommentSerializer  
# from .permissions import IsAuthorEditorPermission  # Import your custom permission (if you have one)


User = get_user_model()
 


class IsAuthorGroupWithModelPermission(permissions.DjangoModelPermissions):
    # Permission to allow author to edit and "staffposteditor" to delete comment only.
    """
    Permission to allow author to edit and delete their post only.
    """
     
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # ------------------
        # return True
        # ------------------

        is_author = obj.author == request.user

        print("-----------------------------")
        print(request.user.groups)
        print(request.user.has_perm('blog.delete_post'), "blog.delete_post")
        
        print("-----------------------------")

        is_staffposteditor = request.user.groups.filter(name='staffposteditor').exists() and request.user.has_perm('blog.delete_post')

  

        if request.method in ['PUT', 'PATCH', 'DELETE']:
            # return is_author or is_staffposteditor
            return is_author
        
 

        return False
    
    def has_permission(self, request, view):
        # Allow GET, HEAD, or OPTIONS requests for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # For other methods, fall back to the default DjangoModelPermissions check
        return super().has_permission(request, view)
    

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorGroupWithModelPermission ]

    def perform_update(self, serializer):
        serializer.save()
        return Response({"message": "Post updated successfully."}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"message": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
 
        return Response(serializer.data)


    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all()
        return Post.objects.filter(author=self.request.user)


class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    View for listing and creating posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    authentication_classes = [authentication.SessionAuthentication]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorGroupWithModelPermission]  

    def perform_create(self, serializer):
        """
        Automatically set the author of the post.
        """
        # print(type(self.request.user.id))
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:  # Check if the user is an admin/staff
            return Post.objects.all()
        
        return Post.objects.all()
 
# ---------------------------------------------------------------------------
        

class IsCommentAuthorOrModerator(permissions.BasePermission):
    """
    Permission to allow author to edit/delete their own post and being in  moderators can edit other's comments but not delete it.
    """
    # in admin panel , moderator has "edit only" permission.
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        # 'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        # 'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        is_author = obj.user == request.user
        is_moderator = request.user.groups.filter(name='moderator').exists() and request.user.has_perm('blog.change_comment')

        if request.method in ['PUT', 'PATCH']:
            return is_author or is_moderator
        elif request.method == 'DELETE':
            return is_author
        return False


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCommentAuthorOrModerator]

    def perform_update(self, serializer):
        serializer.save()
        return Response({"message": "Comment updated successfully."}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"message": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class CommentListCreateAPIView(generics.ListCreateAPIView):
    """
    View for listing and creating comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Set the user and post for the comment.
        """
        post_id = self.request.data.get('post')  
        post = get_object_or_404(Post, id=post_id) 
        serializer.save(user=self.request.user, post=post)

    def get_queryset(self):
        # return Comment.objects.filter(post__status='published').filter(post= self.request.user)

        post_id = self.request.query_params.get('post')
        if not post_id:
            return Comment.objects.none()

        post = get_object_or_404(Post, id=post_id, status='published')
        return Comment.objects.filter(post=post)
  

#############################################################
#############################################################
#############################################################
#############################################################
    

from rest_framework import  status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from .serializers import LikeSerializer  

class LikeListCreateAPIView(generics.ListCreateAPIView):
    """
    View for listing likes for a specific post and creating/deleting likes.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]  # User must be logged in to like/unlike

    def get_queryset(self):
        """
        Returns the likes for a specific post.
        The post ID should be passed as a query parameter (e.g., /api/likes/?post=123).
        """
        post_id = self.request.query_params.get('post', None)
        if post_id is not None:
            return Like.objects.filter(post_id=post_id)
        return Like.objects.none()  

    def create(self, request, *args, **kwargs):
        """
        Handles the creation (like) or deletion (unlike) of a like.
        Expects the 'post' ID in the request data.
        """
        post_id = request.data.get('post')
        if not post_id:
            return Response({"error": "Please provide the 'post' ID."}, status=status.HTTP_400_BAD_REQUEST)

        post = get_object_or_404(Post, id=post_id)
        user = self.request.user

        try:
            like = Like.objects.get(post=post, user=user)
            # If the like exists, delete it (unlike)
            like.delete()
            return Response({"message": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            # If the like doesn't exist, create it (like)
            serializer = self.get_serializer(data={'post': post.id, 'user': user.id})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostLikeCountAPIView(APIView):
    """
    Returns the total like count for a specific post.
    """
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like_count = Like.objects.filter(post=post).count()
        return Response({"like_count": like_count})
    


#############################################################
#############################################################
#############################################################
#############################################################
    

from rest_framework import generics, permissions
from rest_framework import filters  # For SearchFilter
from django_filters.rest_framework import DjangoFilterBackend  # For Tag Filtering
from rest_framework.pagination import PageNumberPagination
# from .models import Post, Tag
from .serializers import PostSerializer

class PostPagination(PageNumberPagination):
    """
    Custom pagination class for posts.
    You can adjust the page size here.
    """
    page_size = 8
    page_size_query_param = 'page_size'  # Allows client to override page size
    max_page_size = 100

class PostSearchListAPIView(generics.ListAPIView):
    """
    API view for searching posts.
    """
    # http://127.0.0.1:8000/api/blog/posts/search/?search=88
    # http://127.0.0.1:8000/api/blog/posts/search/?search=pratham

    
    # {
    # "count": 4,
    # "next": "http://127.0.0.1:8000/api/blog/posts/search/?page=2&search=pratham",


    queryset = Post.objects.filter(status='published')  # Only search published posts
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Fields to search in

    def get_queryset(self):
        """
        Optionally filter the queryset based on search query.
        The SearchFilter backend handles this automatically based on 'search_fields'.
        """
        return super().get_queryset()

class PostTagFilterListAPIView(generics.ListAPIView):
    """
    API view for filtering posts by tag.
    """
    # http://127.0.0.1:8000/api/blog/posts/tag/?tags__name=deepseek

    queryset = Post.objects.filter(status='published')  # Only show published posts
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tags__name']  # Filter by tag name

    def get_queryset(self):
        """
        Optionally filter the queryset based on the 'tag__name' query parameter.
        The DjangoFilterBackend handles this automatically based on 'filterset_fields'.
        """
        return super().get_queryset()


#############################################################
#############################################################
#############################################################
#############################################################
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from django.urls import reverse

class AuthorDashboardAPIView(APIView):
    """
    Returns stats and recent data for the author's dashboard.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        post_count = Post.objects.filter(author=user).count()
        comment_count = Comment.objects.filter(post__author=user).count()
       
        recent_unpublished_posts = Post.objects.filter(author=user, status='draft').order_by('-created_at')[:5]
        recent_unpublished_data = [
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author.name,
                # "created_at": post.created_at,
            }
            for post in recent_unpublished_posts
        ]

        create_post_url = reverse('post-list-create')  # Make sure your URL patterns have this name

        return Response({
            "post_count": post_count,
            "comment_count": comment_count,
            "recent_unpublished_posts": recent_unpublished_data,
            "create_post_url": request.build_absolute_uri(create_post_url),
        })


#############################################################
#############################################################
#############################################################
#############################################################
    



# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Post, GroupProfile

class GroupPermissionAPIView(APIView):
    # {"group": "staffposteditor", "permissions": [ "change", "delete"] }
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def post(self, request):
        group_name = request.data.get("group")
        actions = request.data.get("permissions", [])

        if not group_name or not isinstance(actions, list):
            return Response({"error": "Invalid request data."}, status=status.HTTP_400_BAD_REQUEST)

        group, _ = Group.objects.get_or_create(name=group_name)
        content_type = ContentType.objects.get_for_model(Post)

        added_perms = []
        for action in actions:
            codename = f"{action}_post"
            try:
                perm = Permission.objects.get(codename=codename, content_type=content_type)
                group.permissions.add(perm)
                added_perms.append(codename)
            except Permission.DoesNotExist:
                continue

        return Response({"message": f"Permissions added to group '{group_name}'", "added": added_perms})

    def delete(self, request):
        group_name = request.data.get("group")
        actions = request.data.get("permissions", [])

        if not group_name or not isinstance(actions, list):
            return Response({"error": "Invalid request data."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            return Response({"error": f"Group '{group_name}' not found."}, status=status.HTTP_404_NOT_FOUND)

        content_type = ContentType.objects.get_for_model(Post)
        removed_perms = []
        for action in actions:
            codename = f"{action}_post"
            try:
                perm = Permission.objects.get(codename=codename, content_type=content_type)
                group.permissions.remove(perm)
                removed_perms.append(codename)
            except Permission.DoesNotExist:
                continue

        return Response({"message": f"Permissions removed from group '{group_name}'", "removed": removed_perms})


class GroupListCreateAPIView(APIView):
         
    permission_classes = [IsAdminUser]

    def get(self, request):
        groups = Group.objects.all()
        data = [{"name": group.name, "description": getattr(group.profile, 'description', '')} for group in groups]
        return Response(data)

    def post(self, request):
        name = request.data.get("name")
        description = request.data.get("description", "")

        if not name:
            return Response({"error": "Group name is required."}, status=status.HTTP_400_BAD_REQUEST)

        group, created = Group.objects.get_or_create(name=name)
        GroupProfile.objects.update_or_create(group=group, defaults={"description": description})

        return Response({"message": f"Group '{name}' created or updated."})


class GroupMembershipAPIView(APIView):
 
    permission_classes = [IsAdminUser]

    def post(self, request):
        name = request.data.get("name")
        group_name = request.data.get("group")

        try:
            user = User.objects.get(name=name)
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            return Response({"message": f"User '{name}' added to group '{group_name}'."})
        except (User.DoesNotExist, Group.DoesNotExist):
            return Response({"error": "User or group not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        name = request.data.get("name")
        group_name = request.data.get("group")

        try:
            user = User.objects.get(name=name)
            group = Group.objects.get(name=group_name)
            user.groups.remove(group)
            return Response({"message": f"User '{name}' removed from group '{group_name}'."})
        except (User.DoesNotExist, Group.DoesNotExist):
            return Response({"error": "User or group not found."}, status=status.HTTP_404_NOT_FOUND)


