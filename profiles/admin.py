from django.contrib import admin

from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'address', 'city', 'state', 'contact_no',)
    search_fields = ('user__email', 'first_name', 'last_name', 'email', 'firm__firm_name', 'city')


admin.site.register(Profile, ProfileAdmin)
