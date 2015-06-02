from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import os
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/home/ronan/wiki_project/media/photos')

def get_image_path(instance,filename):
   return os.path.join('photos', str(instance.user.id), filename)

class UserProfile(models.Model):
    #EXTENDED USER CLASS
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    birthdate = models.DateField(null=True)
    description = models.TextField(default='')  #SHORT DESCRIPTION OF THE USER
    ip_address = models.TextField(default='0.0.0.0')
    user_auth = models.IntegerField(default=1)
    

    def __unicode__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_profile_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            UserProfile.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_profile_for_user(sender, instance=None, **kwargs):
        if instance:
            user_profile = UserProfile.objects.get(user=instance)
            user_profile.delete()