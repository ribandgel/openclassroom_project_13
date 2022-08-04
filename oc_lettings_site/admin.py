from django.contrib import admin

from oc_lettings_site.lettings.models import Letting, Address
from oc_lettings_site.profiles.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
