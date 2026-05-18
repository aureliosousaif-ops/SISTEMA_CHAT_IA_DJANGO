from django.shortcuts import render

from .services.ai_service import get_ai_response

from .models import Message


def chat_view(request):

    # Busca histórico
    messages = Message.objects.all().order_by('created_at')

    if request.method == 'POST':

        # Mensagem usuário
        user_message = request.POST.get('message')

        # Resposta IA
        response = get_ai_response(user_message)

        # Salva no banco
        Message.objects.create(

            user_message=user_message,

            ai_response=response

        )

    # Atualiza histórico
    messages = Message.objects.all().order_by('created_at')

    return render(request, 'chat/chat.html', {

        'messages': messages

    })