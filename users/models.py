# Importa models do Django
from django.db import models


# =========================
# MODEL ALUNO
# =========================
class Student(models.Model):

    # Nome aluno
    name = models.CharField(max_length=255)

    # Número matrícula
    registration = models.CharField(
        max_length=50,
        unique=True
    )

    # Data nascimento
    birth_date = models.DateField()

    # Turma aluno
    classroom = models.CharField(
        max_length=100
    )

    # Data criação
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # Nome amigável admin
    def __str__(self):

        return self.name


# =========================
# MODEL PROFESSOR
# =========================
class Teacher(models.Model):

    # Nome professor
    name = models.CharField(max_length=255)

    # Código CEAP
    ceap = models.CharField(
        max_length=50,
        unique=True
    )

    # Data nascimento
    birth_date = models.DateField()

    # Matéria professor
    subject = models.CharField(
        max_length=100
    )

    # Data criação
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # Nome amigável admin
    def __str__(self):

        return self.name