# Importa models do Django
from django.db import models

# Importa função que lê PDFs
from .services.pdf_reader import extract_text_from_pdf


# Classe Material
class Material(models.Model):

    # Título do material
    title = models.CharField(max_length=255)

    # Nome da matéria
    subject = models.CharField(max_length=255)

    # Upload do PDF
    file = models.FileField(upload_to='pdfs/')

    # Texto extraído do PDF
    extracted_text = models.TextField(blank=True)

    # Data upload
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # Método executado ao salvar objeto
    def save(self, *args, **kwargs):

        print("SAVE FOI CHAMADO")

        # Salva primeiro o arquivo PDF
        super().save(*args, **kwargs)

        # Verifica se existe arquivo
        if self.file:

            print("PDF ENCONTRADO")

            # Caminho completo do PDF
            pdf_path = self.file.path

            print(pdf_path)

            # Extrai texto
            extracted_text = extract_text_from_pdf(pdf_path)

            print("TEXTO EXTRAÍDO:")
            print(extracted_text)

            # Salva texto no campo
            self.extracted_text = extracted_text

            # Atualiza banco
            super().save(update_fields=['extracted_text'])

    # Nome amigável no admin
    def __str__(self):
        return self.title