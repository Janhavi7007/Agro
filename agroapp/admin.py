from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, GovernmentScheme, AgroBusiness

# CustomUser Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'username', 'full_name', 'email', 'phone_number', 'is_superuser', 'is_staff')
    search_fields = ('username', 'email', 'full_name', 'phone_number')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# GovernmentScheme Admin
class GovernmentSchemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'apply_link')
    search_fields = ('title', 'state')

admin.site.register(GovernmentScheme, GovernmentSchemeAdmin)

# AgroBusiness Admin
@admin.register(AgroBusiness)
class AgroBusinessAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost_to_implement', 'profit')
    search_fields = ('title',)


from django.contrib import admin
from .models import OrganicFarmingCategory

# Register the OrganicFarmingCategory model
admin.site.register(OrganicFarmingCategory)


from django.contrib import admin
from .models import Feedback

from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'submitted_at', 'admin_reply')
    list_filter = ('submitted_at',)


from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')

admin.site.register(ContactMessage, ContactMessageAdmin)