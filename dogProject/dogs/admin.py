from django.contrib import admin

# Register your models here.

# setting up admin so that I can add information and make changes
from.models import Dog
admin.site.register(Dog)

from.models import Account
admin.site.register(Account)

