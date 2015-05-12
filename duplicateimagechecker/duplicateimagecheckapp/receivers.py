"""
Recievers for django signals

"""
from django.db.models.signals import post_save
from django.dispatch import receiver

from duplicateimagecheckapp.models import ImageDupe
from duplicateimagecheckapp.tasks import calculate_hash

@receiver(post_save, sender=ImageDupe)
def impage_dupe_save(sender, instance, **kwargs):
    """
    Post save hook that kicks off job to calculate perceptual hash if none exists yet.

    Assumes if a hash is already avaiable on image, then we don't need to recaculate.

    """
    # kick off job to calculate image perceptual hash if hash is missing
    if instance and instance.image and instance.image.url and not instance.image_hash:
        calculate_hash.apply_async(kwargs={'primary_key': instance.pk})