from django.contrib import admin
from .models import Post, Checkin, Message
# Register your models here.


@admin.register(Checkin)
class checkinAdmin(admin.ModelAdmin):
    list_display = ('username', 'x', 'y', 'cheek_date')
    list_filter = ('username', 'x')
    # date_hierarchy = 'date'
    # ordering = ('date', )
    search_fields = ('username', 'x')


admin.site.register(Post)
admin.site.register(Message)
