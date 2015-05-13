"""
Setup/registration for admin app

"""
from django.contrib import admin

from duplicateimagecheckapp.models import ImageDupe

class ImageDupeAdmin(admin.ModelAdmin):
    """
    Model admin to customize list display in admin list view of ImageDupe model

    """
    list_display = ('id', 'image_img', 'is_duplicate', 'image_hash')

admin.site.register(ImageDupe, ImageDupeAdmin)