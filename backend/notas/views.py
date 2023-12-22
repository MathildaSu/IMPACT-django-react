from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Nota
from .forms import NotaForm


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the Notas index.</h1>")


def notas_list(request):
    notas = Nota.objects.all()
    return render(request, 'notas_list.html', {'notas': notas})


def create_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notas_list')
    else:
        form = NotaForm()
    return render(request, 'create_nota.html', {'form': form})

def edit_nota(request, pk):
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
    nota = nota.objects.get(pk=pk)
    if request.method == 'POST':
        nota.delete()
        return redirect('notas_list')
    return render(request, 'delete_nota.html', {'nota': nota})