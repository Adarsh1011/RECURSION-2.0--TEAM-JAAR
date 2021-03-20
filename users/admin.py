from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('user_name', 'email', 'is_hospital',)
    list_filter = ('user_name', 'email', 'is_hospital', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('user_name', 'email', 'is_hospital',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('user_name', 'email', 'is_hospital',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'email', 'is_hospital', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)