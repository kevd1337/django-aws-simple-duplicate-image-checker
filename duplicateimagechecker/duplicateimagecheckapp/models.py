"""
Models for duplicateimagecheckapp

"""
from uuid import uuid4

from django_boto.s3.storage import S3Storage

from django.db import models

# S3 storage object, used for images
s3 = S3Storage()

def image_upload_to_path(instance, filename):
    """ 
    Helper function that generates a s3 prefix for given image.

    """
    ext = filename.split('.')[-1]
    return '{}.{}'.format(uuid4().hex, ext)

class ImageDupe(models.Model):
    image = models.ImageField(storage=s3, upload_to=image_upload_to_path)
    is_duplicate = models.BooleanField(default=False)
    image_hash = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Overriding save to clear image hash if image changed.
        
        """
        if self.pk is not None:
            orig = ImageDupe.objects.get(pk=self.pk)        
            if self.image != orig.image:
                # Image changed, so remove hash for recalculation later
                self.is_duplicate = False
                self.image_hash = None
        super(ImageDupe, self).save(*args, **kwargs) 
