from django.contrib import admin
from .models import AgainVerifyMembership


class UserImageAdmin(admin.ModelAdmin):
    class Meta:
        model = AgainVerifyMembership

admin.site.register(AgainVerifyMembership, UserImageAdmin)
