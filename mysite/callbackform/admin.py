from django.contrib import admin
from .models import CallbackForm




class CallBackFormAdmin(admin.ModelAdmin):
    list_display=['subject','archive','name','comment','support_datetime','create_date']
    list_filter =['archive']
    ordering = ['support_datetime','create_date']


# Register your models here.
admin.site.register(CallbackForm,CallBackFormAdmin)