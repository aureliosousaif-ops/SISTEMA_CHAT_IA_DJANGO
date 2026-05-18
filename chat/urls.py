# Importa função path
from django.urls import path

# Importa views
from . import views


# Lista de URLs do app chat
urlpatterns = [

    # URL principal do chat
    # /chat/
    path('', views.chat_view, name='chat'),
]