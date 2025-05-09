from django.contrib import admin
from users.models import User
from core.models import Program

admin.site.register(User)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'desc', 'full_info', 'start_date', 'end_date']
    prepopulated_fields = {'slug': ('title',)}  # Title ga qarab slugni avtomatik to'ldiradi

admin.site.register(Program, ProgramAdmin)
