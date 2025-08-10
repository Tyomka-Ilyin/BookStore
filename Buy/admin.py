from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import Buy, structureBuy, discount

admin.site.register(Buy)
admin.site.register(structureBuy)
admin.site.register(discount)

