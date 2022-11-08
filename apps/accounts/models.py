from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

ClassChoices = [
    ("Ecanomy" , "Ecanomy"),
    ("First" , "First"),
    ("Business" , "Business")

]
class Flight(models.Model):
    From = models.CharField(_("Qayerdan"),max_length = 50,blank=False)
    to = models.CharField(_("Qayerga"),max_length = 50,blank=False)
    outbound = models.DateTimeField(_("Boshlanish vaqti"),blank=False)
    Return = models.DateTimeField(_("Qaytish vaqti"),auto_now_add=True,blank=False)
    children = models.IntegerField(_("Bolalar soni"),blank=False)
    Class = models.CharField(_("Klass"),choices=ClassChoices,blank=False)
    price = models.IntegerField(_("Narxi"),blank=False)
    count = models.IntegerField(_("Joylar soni"),blank=False)

    def __str__(self):
        return self.From
class Country(models.Model):
    name = models.Model(_("Nomi"),max_length=50,blank=False)

class Hotel(models.Model):
    name = models.CharField(_("Mehmonxona nomi"),max_length=50,blank=False)
    rooms = models.IntegerField(_("Xonalar soni"),blank=False)
    price = models.IntegerField(_("Narxi"),blank=False)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(_("Ism"),max_length=60)
    email = models.EmailField(_("Emailni kiriting"))
    massage = models.CharField(_("Textni kiriting"),max_length=100)

    def __str__(self):
        return self.name
class Book(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)

    def __str__(self):
        return self.user





