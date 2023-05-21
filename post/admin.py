from django.contrib import admin
from .models import Post,Comment,Category
# Register your models here.

# Custom admin configuration for the Post model.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','image')
    search_fields = ('title', 'content',)
    list_filter = ('created_at',)

    exclude = ('slug',)

# Register the Post model with the custom admin configuration
admin.site.register(Post, PostAdmin)

# Custom admin configuration for the Comment model.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','content','created_at')
    search_fields = ('post','content',)
    list_filter = ('created_at',)


# Register the Comment model with the custom admin configuration
admin.site.register(Comment, CommentAdmin)

# Register the Category model
admin.site.register(Category)