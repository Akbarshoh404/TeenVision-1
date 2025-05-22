from django.contrib import admin
from django.contrib.auth import get_user_model
from core.models import Program, Major

User = get_user_model()


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'desc', 'full_info', 'created_at']
    prepopulated_fields = {'slug': ('title',)}  # Title ga qarab slugni avtomatik to'ldiradi

admin.site.register(Program, ProgramAdmin)
admin.site.register(User)
admin.site.register(Major)