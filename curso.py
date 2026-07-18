from pathlib import Path
import json

# ==========================================
# CURSO ACTIVO
# ==========================================

BASE = Path("cursos") / "incendios"

# ==========================================
# DATOS GENERALES
# ==========================================

def obtener_nombre():
    return "Prevención y Combate de Incendios"


def obtener_tema():
    return "Triángulo del Fuego"


# ==========================================
# LECCIÓN
# ==========================================

def obtener_leccion():

    archivo = BASE / "leccion1.md"

    return archivo.read_text(
        encoding="utf-8"
    )


# ==========================================
# PREGUNTAS
# ==========================================

def obtener_preguntas():

    archivo = BASE / "preguntas.json"

    with open(
        archivo,
        encoding="utf-8"
    ) as f:

        return json.load(f)


# ==========================================
# IMAGEN
# ==========================================

def obtener_imagen():

    return BASE / "imagenes" / "triangulo_fuego.png"