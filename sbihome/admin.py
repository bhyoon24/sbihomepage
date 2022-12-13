from django.contrib import admin
from .models import member

class MemberAdmin(admin.ModelAdmin):
    list_display = ['member_name', 'member_cellphone', 'regdate', 'member_email']
    # raw_id_fields = ['member_name', 'member_cellphone']
    list_filter = ['member_name', 'member_cellphone', 'regdate']
    search_fields = ['member_name', 'member_cellphone']
    ordering = ['-regdate']

admin.site.register(member, MemberAdmin)
# Register your models here.
