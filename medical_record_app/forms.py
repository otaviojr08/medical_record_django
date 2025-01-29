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
        fields = ['medico', 'paciente', 'tipo', 'descricao']

    def __init__(self, *args, exibir_medico=True, exibir_paciente=True, **kwargs):
        super().__init__(*args, **kwargs)

        if not exibir_paciente:
            del self.fields['paciente']  # Remove o campo de paciente se não for necessário

        if not exibir_medico:
            del self.fields['medico']  # Remove o campo de médico se não for necessário
        

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['nome', 'resultado', 'data_realizacao']
