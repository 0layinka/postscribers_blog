from django.contrib import admin
from .models import profileModel

# Register your models here.
@admin.register(profileModel)
class profileAdmin(admin.ModelAdmin):
    pass
