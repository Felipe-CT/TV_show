from __future__ import unicode_literals
from django.db import models

class valManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title']= "Titulo debe tener al menos 2 caracteres"
        if len(post_data['network']) < 3:
            errors["network"] = "Canal debe tener al menos 2 caracteres"
        if len(post_data['desc']) < 10:
            errors["desc"] = "La descripcion debe ser de al menos 10 caracteres"
        return errors

class Show(models.Model):

    title = models.CharField(max_length=200)
    network = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=valManager() 

