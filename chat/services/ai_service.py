# Importa model Material
from materials.models import Material


def split_text(text, chunk_size=500):
    """
    Divide texto em pedaços menores
    """

    chunks = []

    # Percorre texto
    for i in range(0, len(text), chunk_size):

        # Cria pedaço
        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


def get_ai_response(user_message):
    """
    Busca inteligente no PDF
    """

    # Busca materiais
    materials = Material.objects.all()

    # Melhor resultado encontrado
    best_match = None

    # Maior pontuação
    best_score = 0

    # Percorre materiais
    for material in materials:

        # Divide texto em chunks
        chunks = split_text(material.extracted_text)

        # Percorre chunks
        for chunk in chunks:

            score = 0

            # Divide pergunta em palavras
            words = user_message.lower().split()

            # Conta quantas palavras aparecem
            for word in words:

                if word in chunk.lower():
                    score += 1

            # Verifica melhor resultado
            if score > best_score:

                best_score = score

                best_match = {
                    'material': material.title,
                    'chunk': chunk
                }

    # Se encontrou resultado
    if best_match:

        return f"""
Material encontrado: {best_match['material']}

Trecho relevante:

{best_match['chunk']}
"""

    # Caso não encontre
    return "Não encontrei resposta nos materiais."