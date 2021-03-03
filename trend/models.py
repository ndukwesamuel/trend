from django.db import models

# Create your models here.



class contactModel(models.Model):

    Name = models.CharField(max_length=100, null=True)
    Email = models.CharField(max_length=100, null=True)
    Ask_us_anything = models.TextField(null=True)

    def __str__(self):
        return self.Name
