from django.contrib import admin
from .models import Paciente, Medico, Prontuario, Exame

# Registro da model Paciente
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'sexo', 'telefone', 'email')  # Campos que serão exibidos na lista
    search_fields = ('nome', 'email', 'telefone')  # Campos para buscar
    list_filter = ('sexo',)  # Filtros disponíveis na barra lateral
    ordering = ('nome',)  # Ordenação padrão

# Registro da model Medico
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'especialidade', 'telefone', 'email')
    search_fields = ('nome', 'crm', 'especialidade', 'email')
    list_filter = ('especialidade',)
    ordering = ('nome',)

# Registro da model Prontuario
@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'tipo', 'data', 'descricao')
    search_fields = ('paciente__nome', 'medico__nome', 'descricao')  # Pesquisa em campos relacionados
    list_filter = ('tipo', 'data')
    ordering = ('-data',)  # Ordenar por data mais recente

# Registro da model Exame
@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
    list_display = ('nome', 'prontuario', 'data_realizacao', 'resultado')
    search_fields = ('nome', 'prontuario__paciente__nome', 'resultado')  # Pesquisa nos campos relacionados
    list_filter = ('data_realizacao',)
    ordering = ('-data_realizacao',)  # Ordenar por data mais recente
