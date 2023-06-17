from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('id', "phone", 'email', "rating", 'password', 'staff', 'is_active',)
    list_filter = ('email', 'staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ("phone", 'email', "rating", 'password', 'avatar', 'firstname', 'lastname')}),
        ('Permissions', {'fields': ('staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("phone", 'email', "rating", 'password1', 'password2', 'avatar', 'staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
