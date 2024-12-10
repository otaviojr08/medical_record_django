from django import forms
from .models import Paciente, Medico, Prontuario, Exame

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'sexo', 'endereco', 'telefone', 'email']


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'especialidade', 'telefone', 'email']


class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = ['medico', 'tipo', 'descricao']


class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['nome', 'resultado', 'data_realizacao']
