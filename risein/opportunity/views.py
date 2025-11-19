from django.shortcuts import render
from .models import Vaga
from .forms import FiltroForm
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .forms import VagaForm
from django.contrib.auth.decorators import login_required


def home(request):
    form = FiltroForm(request.GET or None)
    vagas = Vaga.objects.all()

    if form.is_valid():
        busca = form.cleaned_data.get('busca')
        localizacao = form.cleaned_data.get('localizacao')
        tipo = form.cleaned_data.get('tipo')
        remoto = form.cleaned_data.get('remoto')


        if busca:
            vagas = vagas.filter(titulo__icontains=busca)
        if localizacao:
            vagas = vagas.filter(localizacao__icontains=localizacao)
        if tipo:
            vagas = vagas.filter(tipo__in=tipo)
        if remoto:
            vagas = vagas.filter(remoto=True)


    return render(request, 'opportunity/home.html', {'form': form, 'vagas': vagas})


@staff_member_required
def criar_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VagaForm()

    return render(request, 'opportunity/criar_vaga.html', {'form': form})

def vaga_detail(request, id):
    vaga = get_object_or_404(Vaga, id=id)
    return render(request, 'opportunity/vaga_detail.html', {'vaga': vaga})

@login_required
def editar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == 'POST':
        form = VagaForm(request.POST, instance=vaga)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = VagaForm(instance=vaga)
    return render(request, 'opportunity/criar_vaga.html', {'form': form})

@login_required
def excluir_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    vaga.delete()
    return redirect('home')
