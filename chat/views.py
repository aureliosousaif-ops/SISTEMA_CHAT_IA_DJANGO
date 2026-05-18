from django.shortcuts import render, redirect

from .services.ai_service import get_ai_response

from .models import Message


# =========================
# CHAT IA
# =========================
def chat_view(request):

    # Verifica login
    if 'student_id' not in request.session:

        return redirect('/login/aluno/')

    # Busca histórico
    messages = Message.objects.all().order_by('created_at')

    # Verifica formulário
    if request.method == 'POST':

        # Mensagem usuário
        user_message = request.POST.get('message')

        # Resposta IA
        response = get_ai_response(user_message)

        # Salva banco
        Message.objects.create(

            user_message=user_message,

            ai_response=response

        )

    # Atualiza histórico
    messages = Message.objects.all().order_by('created_at')

    return render(

        request,

        'chat/chat.html',

        {

            'messages': messages,

            # Nome aluno
            'student_name': request.session.get(
                'student_name'
            )

        }

    )