from django.contrib import admin
from .models import Users1
@admin.register(Users1)

class UserAdmin(admin.ModelAdmin):
    list_display=('name','email','password','author')