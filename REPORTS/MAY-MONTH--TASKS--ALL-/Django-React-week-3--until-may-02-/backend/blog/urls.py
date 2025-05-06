from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostDetailAPIView,
    # PostUpdateAPIView,
    # PostDestroyAPIView,
    CommentListCreateAPIView,
    CommentDetailAPIView,

    #
    LikeListCreateAPIView,
    PostLikeCountAPIView,

    #
    PostSearchListAPIView,
    PostTagFilterListAPIView,

    #
    GroupPermissionAPIView,
    GroupListCreateAPIView,
    GroupMembershipAPIView,

    #
    AuthorDashboardAPIView


)

urlpatterns = [

    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    # path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),

    path('posts/<uuid:pk>/', PostDetailAPIView.as_view(), name='post-detail'),

 
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<uuid:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),

    #
    path('likes/', LikeListCreateAPIView.as_view(), name='post-likes'),
    path('posts/<uuid:post_id>/likes/count/', PostLikeCountAPIView.as_view(), name='post-like-count'),

    #
    path('posts/search/', PostSearchListAPIView.as_view(), name='post-search-api'),
    path('posts/tag/', PostTagFilterListAPIView.as_view(), name='post-tag-filter-api'),

    #
    path('author/dashboard/', AuthorDashboardAPIView.as_view(), name='author-dashboard'),



    # group
    path('groups/', GroupListCreateAPIView.as_view(), name='group-list-create'),
    path('groups/permissions/', GroupPermissionAPIView.as_view(), name='group-permission'),
    path('groups/members/', GroupMembershipAPIView.as_view(), name='group-membership'),
]


 