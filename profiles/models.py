from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings


User._meta.get_field('email')._unique = True
User._meta.get_field('email').null = False
User._meta.get_field('email').blank = False


class Profile(models.Model):

    """User profile"""

    user = models.ForeignKey(User)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    contact_no = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    skype_id = models.CharField(max_length=50, blank=True, null=True)
    linkedin_id = models.CharField(max_length=50, blank=True, null=True)
    bitbucket_id = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    primary_skills = models.CharField(max_length=255, blank=True, null=True)
    secondary_skills = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True, verbose_name="DateOfBirth")
    is_deleted = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_record(sender, instance, created, **kwargs):
    profile_obj, created = Profile.objects.get_or_create(user=instance)


post_save.connect(create_record, sender=User)
