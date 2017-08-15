from django.contrib import admin
from .models import User


@admin.register(User)
class usersAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'password')
    list_filter = ('username', 'lastname',)
    # date_hierarchy = 'date'
    # ordering = ('date', )
    search_fields = ('username', 'lastname')
