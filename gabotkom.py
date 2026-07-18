# ==========================================
# GABOTKOM
# Motor principal de la plataforma
# ==========================================

from curso import (
    obtener_leccion,
    obtener_preguntas,
    obtener_nombre,
    obtener_tema
)

from ia import responder


class GaBotKom:

    def __init__(self):

        self.curso = obtener_nombre()

        self.tema = obtener_tema()

        self.leccion = obtener_leccion()

        self.preguntas = obtener_preguntas()

        self.numero_leccion = 1

        self.total_lecciones = 6

        self.historial = []

    # =====================================

    def agregar_historial(self, rol, mensaje):

        self.historial.append({

            "rol": rol,

            "mensaje": mensaje

        })

    # =====================================

    def conversar(self, mensaje_usuario):

        # guardar pregunta del usuario
        self.agregar_historial(

            "usuario",

            mensaje_usuario

        )

        # obtener respuesta IA
        respuesta = responder(
            pregunta=mensaje_usuario,
            respuesta_usuario=mensaje_usuario,
            contenido=self.leccion
        )   

        # guardar respuesta
        self.agregar_historial(

            "gabotkom",

            respuesta

        )

        return respuesta

    # =====================================

    def obtener_historial(self):

        return self.historial

    # =====================================

    def progreso(self):

        return self.numero_leccion / self.total_lecciones