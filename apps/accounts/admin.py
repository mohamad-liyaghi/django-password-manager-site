from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "nick_name")
    readonly_fields = ("email", "nick_name")

admin.site.register(User, UserAdmin)
