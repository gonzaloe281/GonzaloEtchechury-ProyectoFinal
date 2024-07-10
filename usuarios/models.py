from django.db import models
from django.contrib.auth.models import User

class MetaDataUsuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
    hobbie = models.CharField(max_length=100, blank=True, null=True)
=======
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
