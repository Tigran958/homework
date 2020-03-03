from django.contrib import admin
from .models import Customer, Agreement, Balance

admin.site.register(Customer)
admin.site.register(Agreement)
admin.site.register(Balance)

# Register your models here.
