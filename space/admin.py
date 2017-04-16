from django.contrib import admin
from .models import post
from .models import cheekin
# Register your models here.



class cheekinAdmin(admin.ModelAdmin):
	list_display = ('username', 'x', 'y','cheek_date')
	list_filter = ('username','x')
	#date_hierarchy = 'date'
	#ordering = ('date', )
	search_fields = ('username','x')

admin.site.register(cheekin, cheekinAdmin)
admin.site.register(post)
