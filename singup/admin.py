from django.contrib import admin
from .models import users


class usersAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'password')
    list_filter = ('username', 'lastname',)
    # date_hierarchy = 'date'
    # ordering = ('date', )
    search_fields = ('username', 'lastname')


admin.site.register(users, usersAdmin)
