# Importa models
from django.db import models


# Modelo de mensagens do chat
class Message(models.Model):

    # Pergunta do usuário
    user_message = models.TextField()

    # Resposta da IA
    ai_response = models.TextField()

    # Data da conversa
    created_at = models.DateTimeField(auto_now_add=True)

    # Nome amigável no admin
    def __str__(self):

        return self.user_message[:50]