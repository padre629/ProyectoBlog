from django.db import models
from django.conf import settings

#USER table
class Usuario(models.Model):
  idUsu = models.AutoField(primary_key=True)
  nombreUsu = models.CharField(max_length=40)
  usernameUsu = models.CharField(max_length=40)
  passwordUsu = models.CharField(max_length=40)
  class Meta:
    db_table = "usuario"

#class that represents the POST made by an USER
class Publicacion(models.Model):
  idPubli = models.AutoField(primary_key=True)
  contenidoPubli = models.TextField(max_length=300)
  numeroLikesPubli = models.IntegerField(max_length=99)
  fechaPubli = models.CharField(max_length=20)
  publicadorPubli = models.ForeignKey(settings.AUTH_USER_MODEL)
  class Meta:
    db_table = "publicacion"

#class that represents a COMMENT into a POST made by an USER
class Comentario(models.Model):
  idComent = models.AutoField(primary_key=True)
  contenidoComent = models.TextField(max_length=300)
  fechaComent = models.CharField(max_length=20)
  #user that make a comment
  publicadorComent = models.ForeignKey(settings.AUTH_USER_MODEL)
  #a comment belongs to a post
  publicacionComent = models.ForeignKey(Publicacion)
  class Meta:
    db_table = "comentario"
    #http://stackoverflow.com/questions/44109/extending-the-user-model-with-custom-fields-in-django
    #http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance/
    #http://www.b-list.org/weblog/2006/jun/06/django-tips-extending-user-model/