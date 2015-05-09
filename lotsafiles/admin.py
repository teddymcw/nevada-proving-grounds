from django.contrib import admin
from .models import VerifyMembership


class UserImageAdmin(admin.ModelAdmin):
    class Meta:
        model = VerifyMembership

admin.site.register(VerifyMembership, UserImageAdmin)
