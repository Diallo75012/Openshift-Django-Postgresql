from django.db import models
from django.contrib.auth.models import User  # import the built-in User model


class StockInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # User can have one Client and a Client one User only. null=True is to bypass the error on creation and can be deleted after.
    codeAction = models.CharField(max_length=15, blank=True, null=True)
    pays = models.CharField(max_length=30, blank=True, null=True)
    industrie = models.CharField(max_length=30, blank=True, null=True)
    resultat = models.CharField(max_length=15, blank=True, null=True)
    CHOIX = (
    ("BON", "Bon"),
    ("MAUVAIS", "Mauvais"),
    ("A SUIVRE", "A Suivre"),
    )
    potentiel = models.CharField(max_length=9, choices=CHOIX, default="A SUIVRE")
    montantDividende = models.CharField(max_length=15,blank=True, null=True)
    commentaires =  models.CharField(max_length=150, blank=True, null=True)
    recordDate = models.DateTimeField(auto_now=True)
