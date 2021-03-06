from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff',)


admin.site.register(User, UserAdmin)
