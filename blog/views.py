from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import Usuario, Publicacion, Comentario
#django login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_view(request):
  state = "Ingrese sus credenciales para comenzar"
  username = password = ""
  if request.POST: 
    #get user and pass and validate them
    username = request.POST.get("username")
    password = request.POST.get("password")
    #authenticate 
    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        state = "El usuario SI existe y esta activo"
        login(request, user)
        return HttpResponseRedirect("/")
    else:
      state = "Credenciales no validas!"
  #display login form, no post and get requests detected
  return render_to_response("login.html", {"state": state})


@login_required(login_url = "/login/")
def index_view(request):
  return render_to_response('index.html')

def registro_view(request):
  if request.POST: 
    #get user and pass and validate them
    name = request.POST.get("name")
    username = request.POST.get("username")
    pass1 = request.POST.get("pass1")
    pass2 = request.POST.get("pass2")
    #usu = Usuario(nombreUsu=name, usernameUsu=username, passwordUsu=pass1)
    usu = User.objects.create_user(name, username, pass1)
    usu.save()
  return render_to_response('registro.html')