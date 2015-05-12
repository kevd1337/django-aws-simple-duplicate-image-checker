"""
Setup/registration for admin app

"""
from django.contrib import admin

from duplicateimagecheckapp.models import ImageDupe

admin.site.register(ImageDupe)