from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Follow

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('bio', 'location', 'website', 'profilepicture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Follow)
