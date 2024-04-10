from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age', 'is_journalist', 'bookmarked_posts']

    def bookmarked_posts(self, obj):
        return "\n".join([a.title for a in obj.bookmarks.all()])
    
    bookmarked_posts.short_description = 'Bookmarked Posts'
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'is_journalist')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'is_journalist')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)