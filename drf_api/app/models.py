from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=16)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = 'profile'