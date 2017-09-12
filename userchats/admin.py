from django.contrib import admin
from .models import Chat, ChatLine 
# Register your models here.

class ChatAdmin(admin.ModelAdmin):
    list_display = ('chat_id',)

class ChatLineAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'user', 'message', 'created_at')

admin.site.register(Chat, ChatAdmin)
admin.site.register(ChatLine, ChatLineAdmin)