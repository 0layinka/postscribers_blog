from django.contrib import admin
from .models import postModel, comment
# Register your models here.
class postModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')

admin.site.register(postModel, postModelAdmin)

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ( 'author', 'content', 'post')