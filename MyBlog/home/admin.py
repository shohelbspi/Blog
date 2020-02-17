from django.contrib import admin

from .models import Contact
from .models import TeamMember

# Register your models here.
admin.site.register(Contact)
admin.site.register(TeamMember)
