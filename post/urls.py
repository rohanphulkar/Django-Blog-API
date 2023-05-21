from django.urls import path,include
from .views import PostView,CommentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# Register the PostView viewset with the 'posts' endpoin
router.register('posts', PostView,basename="posts")

# Register the CommentView viewset with the 'comments' endpoint
router.register('comments', CommentView,basename="comments")

urlpatterns = [
    # Include the generated URL patterns from the router
    path("",include(router.urls))
]