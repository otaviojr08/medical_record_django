from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    endereco = models.TextField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} ({self.especialidade})"


class Prontuario(models.Model):
    TIPOS = [
        ('consulta', 'Consulta'),
        ('diagnostico', 'Diagnóstico'),
        ('tratamento', 'Tratamento'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='prontuarios')
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, related_name='prontuarios')
    data = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.paciente.nome} - {self.tipo} ({self.data.strftime('%Y-%m-%d')})"


class Exame(models.Model):
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE, related_name='exames')
    nome = models.CharField(max_length=100)
    resultado = models.TextField()
    data_realizacao = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.prontuario.paciente.nome} ({self.data_realizacao})"
