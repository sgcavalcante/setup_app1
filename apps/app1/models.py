from django.db import models

class Contatos(models.Model):
    nome = models.CharField(
        max_length=120,
        null=False,
        blank=False
    )
    fone = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=40
    )

class Contatos1(models.Model):
    nome = models.CharField(
        max_length=120,
        null=False,
        blank=False
    )
    fone = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=40
    )

