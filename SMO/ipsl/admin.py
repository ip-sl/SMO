from django.contrib import admin
from .models import sponsor,protocol,site,screening,day1,day2,day3,day4,day5,day6,EOIV,EOT,TOC,LFU,site_Registration

# Register your models here.

admin.site.register(sponsor)
admin.site.register(protocol)
admin.site.register(site)
admin.site.register(site_Registration)
admin.site.register(screening)
admin.site.register(day1)
admin.site.register(day2)
admin.site.register(day3)
admin.site.register(day4)
admin.site.register(day5)
admin.site.register(day6)
admin.site.register(EOIV)
admin.site.register(EOT)
admin.site.register(TOC)
admin.site.register(LFU)
