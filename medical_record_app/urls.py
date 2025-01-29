from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista_prontuarios/', views.lista_prontuarios, name='lista_prontuarios'),
    path('lista_pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('cadastro_paciente/', views.cadastro_paciente, name='cadastro_paciente'),
    path('paciente/<int:paciente_id>/', views.paciente_detalhes, name='paciente_detalhes'),
    path('lista_medicos/', views.lista_medicos, name='lista_medicos'),
    path('cadastro_medico/', views.cadastro_medico, name='cadastro_medico'),
    path('medico/<int:medico_id>/', views.medico_detalhes, name='medico_detalhes'),
    path('cadastro_prontuario/<int:paciente_id>/', views.cadastro_prontuario_paciente, name='cadastro_prontuario_paciente'),
    path('cadastro_prontuario_medico/<int:medico_id>/', views.cadastro_prontuario, name='cadastro_prontuario'),
    path('prontuario/<int:prontuario_id>/', views.prontuario_detalhes, name='prontuario_detalhes'),
    path('cadastro_exame/<int:prontuario_id>/', views.cadastro_exame, name='cadastro_exame'),
    path('cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

]
