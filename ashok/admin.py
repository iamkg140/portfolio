from django.contrib import admin
# Register your models here.

from .models import *

admin.site.register(Person)
admin.site.register(Social_links)
admin.site.register(Projects)
admin.site.register(Timeline)
admin.site.register(Services)
admin.site.register(Company)
admin.site.register(Contact)


