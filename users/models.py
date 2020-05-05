from django.db import models
from django.contrib.auth.models import User

class Naissance(models.Model):

    TYPES = (
        ('nina','Carte Nina'),
        ('identite','Carte d\'identité'),
        ('passport', 'passeport'),
    )
    prenom = models.CharField(max_length=50,default='')
    nom = models.CharField(max_length=50,default='')
    date = models.DateField(auto_now_add=True)
    prenom_pere = models.CharField(max_length=50,default='')
    nom_pere = models.CharField(max_length=50,default='')
    profession_pere = models.CharField(max_length=50,default='')
    types_piece_pere = models.CharField(max_length=50,choices=TYPES,default='')
    papier_pere = models.ImageField(upload_to = "media/")

    prenom_mere = models.CharField(max_length=50,default='')
    nom_mere = models.CharField(max_length=50,default='')
    profession_mere = models.CharField(max_length=50,default='')
    types_piece_mere = models.CharField(max_length=50,choices=TYPES,default='')
    papier_mere = models.ImageField(upload_to = "media/")

    def __str__(self):
        return f'{self.prenom } {self.nom }'


class Deces(models.Model):
    TYPES = (
        ('nina','Carte Nina'),
        ('identite','Carte d\'identité'),
        ('passport', 'passeport'),
    )
    prenom = models.CharField(max_length=50,default='')
    nom = models.CharField(max_length=50,default='')
    date = models.DateField(auto_now_add=True)
    prenom_pere = models.CharField(max_length=50,default='')
    nom_pere = models.CharField(max_length=50,default='')
    profession_pere = models.CharField(max_length=50,default='')
    types_piece_pere = models.CharField(max_length=50,choices=TYPES,default='')
    papier_pere = models.ImageField()

    prenom_mere = models.CharField(max_length=50,default='')
    nom_mere = models.CharField(max_length=50,default='')
    profession_mere = models.CharField(max_length=50,default='')
    types_piece_mere = models.CharField(max_length=50,choices=TYPES,default='')
    papier_mere = models.ImageField()

    def __str__(self):
        return f'{self.prenom } {self.nom }'

class Utilisateur(models.Model):
    TYPES_ADMIN = (
        ('admin','Admin'),
        ('Opérateur Mairie','Opérateur Mairie'),
        ('Opérateur Centre de Soins', 'Opérateur Centre de Soins'),
    )
    email = models.EmailField()
    telephone = models.CharField(max_length=8)
    statut = models.CharField(max_length=50,choices=TYPES_ADMIN)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.user.username }'