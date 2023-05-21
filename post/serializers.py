from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Post,Comment,Category
from accounts.serializers import UserSerializer

# Serializer for the Comment model.
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

# Serializer for the Category model.
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

# Serializer for the Post model.
class PostSerializer(ModelSerializer):
    category = CategorySerializer(many=False,read_only=True)
    author = UserSerializer(many=False,read_only=True)
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = "__all__"
    
    # Custom method to retrieve comments associated with a post.
    def get_comments(self,obj):
        comments = Comment.objects.filter(post=obj)
        serializer = CommentSerializer(comments,many=True)
        return serializer.data
