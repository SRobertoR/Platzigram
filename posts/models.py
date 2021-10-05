"""Posts Models"""

#Django
from django.db import models
from django.contrib.auth.models import User

from users.models import Profile


class Posts(models.Model):
    """User model"""

    # Cada que se borra el usuario se borran sus posts
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Nombre de la app y el modelo
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="posts/photos")

    #Encuanto se cree una instancia en la base le creara la fecha de cuando se creo
    created = models.DateTimeField(auto_now_add=True)
    #Fecha que se edito por ultima ves 
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""
        return "{} by @{}".format(self.title, self.user.username)



# Create your models here.

"""Posts models"""
# class User (models.Model):
#     """User model"""
#     #Valor unico
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     is_admin = models.BooleanField(default=False)

#     #Puede estar vacia
#     bio = models. TextField(blank=True)
#     #No obligatorio
#     birthdate = models.DateField(blank=True, null=True)



