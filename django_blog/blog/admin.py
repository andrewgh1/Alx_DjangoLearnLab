from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultAdmin
from .models import User,Profile,Post

class UserAdmin(DefaultAdmin):
    list_display = ("username","email","first_name","last_name","is_staff")
    list_filter = ("is_staff","is_superuser","is_active","groups")
    search_fields = ("first_name","last_name","email")

admin.site.register(User,UserAdmin)
admin.site.register(Profile)
admin.site.register(Post)


