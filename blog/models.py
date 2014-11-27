from django.db import models
from django.contrib.auth.models import User

#USER table 
#class Usuario(models.Model):
  #idUsu = models.AutoField(primary_key=True)
  #nombreUsu = models.CharField(max_length=40)
  #usernameUsu = models.CharField(max_length=40)
  #passwordUsu = models.CharField(max_length=40)
  #class Meta:
    #db_table = "usuario"

#class that represents the POST made by an USER
class Publicacion(models.Model):
  idPubli = models.AutoField(primary_key=True)
  contenidoPubli = models.TextField(max_length=300)
  numeroLikesPubli = models.IntegerField(max_length=99)
  fechaPubli = models.CharField(max_length=20)
  publicadorPubli = models.ForeignKey(User)
  class Meta:
    db_table = "publicacion"

#class that represents a COMMENT into a POST made by an USERD
class Comentario(models.Model): 
  idComent = models.AutoField(primary_key=True)
  contenidoComent = models.TextField(max_length=300)
  fechaComent = models.CharField(max_length=20)
  #user that make a comment
  publicadorComent = models.ForeignKey(User)
  #a comment belongs to a post 
  publicacionComent = models.ForeignKey(Publicacion)
  class Meta: 
    db_table = "comentario"
