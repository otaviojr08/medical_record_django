from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente, Medico, Prontuario, Exame
from .forms import PacienteForm, MedicoForm, ProntuarioForm, ExameForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout

# Página inicial
def home(request):
    return render(request, 'home.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Após o cadastro, redireciona para o login
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/cadastro_usuario.html', {'form': form})

# Cadastro de paciente
@login_required
def cadastro_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()

    return render(request, 'user_dashboard/cadastro_paciente.html', { 'form': form })

@login_required
def lista_pacientes(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_paciente')
    else:
        form = PacienteForm()

    pacientes = Paciente.objects.all()
    return render(request, 'user_dashboard/lista_pacientes.html', {
        'form': form,
        'pacientes': pacientes,
    })

# Detalhes do paciente
@login_required
def paciente_detalhes(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    prontuarios = paciente.prontuarios.all()
    return render(request, 'user_dashboard/paciente_detalhes.html', {'paciente': paciente, 'prontuarios': prontuarios})


# Cadastro de médico

@login_required
def lista_medicos(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_medicos')
    else:
        form = PacienteForm()

    medicos = Medico.objects.all()
    return render(request, 'user_dashboard/lista_medicos.html', {
        'form': form,
        'medicos': medicos,
    })


@login_required
def cadastro_medico(request):
    # Processa o formulário
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_medicos')  # Redireciona para a mesma página após salvar
    else:
        form = MedicoForm()  # Formulário vazio para exibição inicial
    
    medicos = Medico.objects.all()
    return render(request, 'user_dashboard/cadastro_medico.html', {'form': form, 'medicos': medicos})

# Detalhes do médico
@login_required
def medico_detalhes(request, medico_id):
    medico = get_object_or_404(Medico, id=medico_id)
    prontuarios = medico.prontuarios.all()
    return render(request, 'user_dashboard/medico_detalhes.html', {'medico': medico, 'prontuarios': prontuarios})


# Cadastro de prontuário
@login_required
def cadastro_prontuario(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = ProntuarioForm(request.POST)
        if form.is_valid():
            prontuario = form.save(commit=False)
            prontuario.paciente = paciente
            prontuario.save()
            return redirect('paciente_detalhes', paciente_id=paciente.id)
    else:
        form = ProntuarioForm()
    return render(request, 'user_dashboard/cadastro_prontuario.html', {'form': form, 'paciente': paciente})


@login_required
def cadastro_prontuario_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = ProntuarioForm(request.POST)
        if form.is_valid():
            prontuario = form.save(commit=False)
            prontuario.paciente = paciente
            prontuario.save()
            return redirect('paciente_detalhes', paciente_id=paciente.id)
    else:
        form = ProntuarioForm()
    return render(request, 'user_dashboard/cadastro_prontuario.html', {'form': form, 'paciente': paciente})


@login_required
def lista_prontuarios(request):
    prontuarios = Prontuario.objects.select_related('paciente').all()
    return render(request, 'user_dashboard/lista_prontuarios.html', {
        'prontuarios': prontuarios
    })

# Detalhes do prontuário
@login_required
def prontuario_detalhes(request, prontuario_id):
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)
    exames = prontuario.exames.all()
    return render(request, 'user_dashboard/prontuario_detalhes.html', {'prontuario': prontuario, 'exames': exames})

# Cadastro de exame
@login_required
def cadastro_exame(request, prontuario_id):
    prontuario = get_object_or_404(Prontuario, id=prontuario_id)
    if request.method == 'POST':
        form = ExameForm(request.POST)
        if form.is_valid():
            exame = form.save(commit=False)
            exame.prontuario = prontuario
            exame.save()
            return redirect('prontuario_detalhes', prontuario_id=prontuario.id)
    else:
        form = ExameForm()
    return render(request, 'user_dashboard/cadastro_exame.html', {'form': form, 'prontuario': prontuario})

def logout_view(request):
    auth_logout(request)
    return redirect('home')
