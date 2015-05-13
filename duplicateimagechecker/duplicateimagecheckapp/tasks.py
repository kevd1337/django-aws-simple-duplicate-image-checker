"""
Celery tasks for app

"""
import os
import urllib
from uuid import uuid4

from celery.decorators import task
import pHash

from duplicateimagecheckapp.models import ImageDupe

@task
def calculate_hash(primary_key):
    """
    Calculates and persists image hash for ImageDupe object referenced by given primary key
    
    """
    instance = ImageDupe.objects.get(pk=primary_key)

    if instance and instance.image and instance.image.url and not instance.image_hash:
        # download image to temporary file
        temp_image_path = '/tmp/{}.{}'.format(uuid4().hex , instance.image.url.split('.')[-1])
        urllib.urlretrieve(instance.image.url, temp_image_path)

        # set image hash (hex of the perceptual hash long integer, with leading 0x and trailing L stripped off)
        image_hash = hex(pHash.imagehash(temp_image_path)).split('x')[-1].split('L')[0]
        instance.image_hash = image_hash

        # check if other object has this hash
        query_set = ImageDupe.objects.filter(image_hash=image_hash).exclude(pk=instance.pk)
        instance.is_duplicate = len(query_set) > 0

        # save image
        instance.save()

        # clean up delete temporary file
        os.remove(temp_image_path)