from django.contrib import admin
from .models import User, Provider


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'display_name')
    readonly_fields = ('created_at', 'updated_at')


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'di', 'provider', 'nickname', 'is_active', 'is_staff', 'created_at')
    list_filter = ('provider', 'is_active', 'is_staff', 'created_at')
    search_fields = ('email', 'nickname', 'di', 'ci')
    ordering = ('-created_at',)
    readonly_fields = ('di', 'created_at', 'updated_at')
    
    fieldsets = (
        ('식별자', {'fields': ('di', 'email')}),
        ('소셜 로그인', {'fields': ('ci', 'provider')}),
        ('개인 정보', {'fields': ('nickname', 'profile_image')}),
        ('권한', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('중요 날짜', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'ci', 'provider', 'nickname'),
        }),
    )


admin.site.register(Provider, ProviderAdmin)
admin.site.register(User, UserAdmin)
