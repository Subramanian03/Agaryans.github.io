from django.contrib import admin
from . models import reg,contacts,adminreg,equipment,package,category,users,reservation,invoice

# Register your models here.
admin.site.register(reg)
admin.site.register(contacts)
admin.site.register(adminreg)
admin.site.register(equipment)
admin.site.register(package)
admin.site.register(category)
admin.site.register(users)
admin.site.register(reservation)
admin.site.register(invoice)
