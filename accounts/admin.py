from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ['email']
	search_fields = ['email']

# Register the User model with the UserAdmin configuration
admin.site.register(User,UserAdmin)