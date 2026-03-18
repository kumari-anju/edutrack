from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'name', 'is_staff', 'is_active']
    search_fields = ('email', 'name')
    ordering = ('email',)
    
    # We don't have username, so we must adjust the fieldsets
    # or Django's built-in UserAdmin will crash looking for 'username'
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
