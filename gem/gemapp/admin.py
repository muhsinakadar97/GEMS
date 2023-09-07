from django.contrib import admin

from .models import Enquiry, Admission

# Register your models here.
admin.site.register(Enquiry),
admin.site.register(Admission),