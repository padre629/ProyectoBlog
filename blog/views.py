from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import Usuario, Publicacion, Comentario
#django login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
#create system users
from django.contrib.auth.models import User


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
  if request.user.is_authenticated():
    nombreUsu = user.username
  return render_to_response('index.html', {'aa':nombreUsu})

def registro_view(request):
  if request.POST:
    #get user and pass and validate them
    name = request.POST.get("name")
    username = request.POST.get("username")
    pass1 = request.POST.get("pass1")
    pass2 = request.POST.get("pass2")
    #system user: (username, email, password)
    usu = User.objects.create_user(name, username, pass1)
    #restrict new users to login into ADMIN page
    usu.is_staff = False
    usu.save()
  return render_to_response('registro.html')

def logout_view(request):
  logout(request)
  return HttpResponseRedirect("/")