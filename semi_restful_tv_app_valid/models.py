from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        if len(post_data['show_title']) < 2:
            errors['title'] = "Show title must be at least 2 characters."

        if len(post_data['show_network']) < 3:
            errors['network'] = "Show network must be at least 3 characters."
            
        if len(post_data['show_description']) < 10 and len(post_data['show_description']) > 0:
            errors['description'] = "Show description must be at least 10 characters."

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add = True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add  = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()