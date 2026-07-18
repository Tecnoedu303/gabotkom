# ===========================================
# VALIDADOR
# ===========================================

def validar_respuesta(texto, palabras):

    texto = texto.lower()

    coincidencias = 0

    for palabra in palabras:

        if palabra.lower() in texto:
            coincidencias += 1

    return coincidencias