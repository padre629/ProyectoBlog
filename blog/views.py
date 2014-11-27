from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import Usuario, Publicacion, Comentario
#django login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
#register
from django.contrib.auth.models import User

def login_view(request):
  state = "Ingrese sus credenciales para comenzar"
  login_ok = None

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
        login_ok = True
        login(request, user)
        return HttpResponseRedirect("/")
    else:
      state = "Credenciales no validas!"
      login_ok = False
  #display login form, no post and get requests detected
  return render_to_response("login.html", {"state": state, "login_ok":login_ok})


@login_required(login_url = "/login/")
def index_view(request):
  return render_to_response('index.html')

def registro_view(request):
  if request.POST:
    #get user and pass and validate them
    name = request.POST.get("name")
    username = request.POST.get("email")
    pass1 = request.POST.get("pass1")
    pass2 = request.POST.get("pass2")
    #system user(username, email, password)
    usu = User.objects.create_user(name, username, pass1)
    usu.is_staff = False
    usu.save()
    return HttpResponseRedirect("/")
  return render_to_response('registro.html')

def logout_view(request):
  logout(request)
  return HttpResponseRedirect("/")