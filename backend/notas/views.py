from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Nota
from .forms import NotaForm

# unused
def index(request):
     return HttpResponse("<h1>Hello, world. You're at the Notas index.</h1>")

def home(request):
    # Get the current user object
    user = request.user
    if not user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    # show home
    return render(request, 'home.html', {"user": user})

def notas_list(request):
     # Get the current user object
    user = request.user
    if not user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    # return list
    notas = Nota.objects.all()
    return render(request, 'notas_list.html', {'notas': notas})

def create_nota(request):
    # Get the current user object
    user = request.user
    if not user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    # do form
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notas_list')
    else:
        form = NotaForm()
    return render(request, 'create_nota.html', {'form': form})

def edit_nota(request, pk):
    # Get the current user object
    user = request.user
    if not user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    nota = Nota.objects.get(pk=pk)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('notas_list')
    else:
        form = NotaForm(instance=Nota)
    return render(request, 'edit_nota.html', {'form': form, 'nota': nota})

def delete_nota(request, pk):
    # Get the current user object
    user = request.user
    if not user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    # do delete
    nota = nota.objects.get(pk=pk)
    if request.method == 'POST':
        nota.delete()
        return redirect('notas_list')
    return render(request, 'delete_nota.html', {'nota': nota})

# Import the login_required decorator and the User model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Define a view that requires the user to be logged in
#@login_required
def profile(request,pk):
    # Get the current user object
    user = request.user
    if not user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    # Render a template with the user's information
    return render(request, "profile.html", {"user": user})


# Define a view that requires the user to have a specific permission
@login_required
def publish(request):
    # Get the current user object
    user = request.user
    # Check if the user has the permission to publish posts
    if user.has_perm("myapp.can_publish"):
        # Render a template with the publishing form
        return render(request, "publish.html")
    else:
        # Return a 403 Forbidden response
        return HttpResponseForbidden("You do not have permission to publish posts.")
