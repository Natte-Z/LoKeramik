from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
   # product = models.ForeignKey('products.Product', on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

    def __str__(self):
        return self.review_title

#class Favourite(models.Model):
 #   """Allows users to have favourite products"""
   # products = models.ManyToManyField(product)
    #current_profile = models.ForeignKey(Profile, related_name='Profile', null=True)

    #@classmethod
    #def make_favourite(cls, current_product), new_favourite):
        #favourite, created = cls.objects_get_or_create(current_product=current_product)
        #favourite.users.add(new_favourite)
    
    #@classmethod
    #def delete_favourite(cls, current_product), new_favourite):
        #favourite, created = cls.objects_get_or_create(current_product=current_product)
        #favourite.users.remove(new_favourite)
