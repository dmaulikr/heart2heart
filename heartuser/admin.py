from django.contrib import admin
from .models import HeartUser, Profile
# Register your models here.
class HeartUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'heartuser', 'profile')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('age', 'ethnicity', 'religion', 'location', 'pets', 'kids')

admin.site.register(HeartUser, HeartUserAdmin)
admin.site.register(Profile, ProfileAdmin)