from rest_framework.response import Response
from .models import Post,Comment
from rest_framework import status,viewsets
from .serializers import PostSerializer,CommentSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Function to retrieve a single object by slug instead of primary key
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Look up the object by slug instead of primary key
        slug = self.kwargs.get('slug')
        if slug is not None:
            queryset = queryset.filter(slug=slug)

        # Get the object
        obj = queryset.get()

        self.check_object_permissions(self.request, obj)

        return obj
    
    # Retrieve a post by its slug
    @action(detail=False, methods=['get'], url_path='slug/(?P<slug>[-\w]+)')
    def retrieve_by_slug(self, request, slug=None):
        queryset = self.get_queryset()
        post = get_object_or_404(queryset, slug=slug)
        serializer = self.get_serializer(post)
        return Response({"data":serializer.data,"status":status.HTTP_200_OK})


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]