# Importa o painel admin do Django
from django.contrib import admin

# Importa o model Material
from .models import Material


# Registra o model no painel admin
# Isso faz o Material aparecer no:
# /admin
admin.site.register(Material)