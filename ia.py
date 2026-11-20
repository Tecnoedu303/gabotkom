import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# CONEXIÓN CON GROQ
# ==========================================

# Identificar de forma segura de dónde viene la clave, sin imprimirla.
try:
    api_key = st.secrets["GROQ_API_KEY"]
    key_source = "st.secrets"
except (KeyError, FileNotFoundError):
    api_key = os.getenv("GROQ_API_KEY")
    key_source = "environment"

if not api_key:
    raise RuntimeError(
        "No se encontró GROQ_API_KEY. "
        "Configura la clave en Streamlit Secrets."
    )

api_key = str(api_key).strip()

# Diagnóstico temporal: nunca registrar la clave ni fragmentos de ella.
print(
    "[GROQ AUTH CHECK] "
    f"source={key_source}; "
    f"length={len(api_key)}; "
    f"has_gsk_prefix={api_key.startswith('gsk_')}; "
    f"has_outer_whitespace={api_key != str(api_key).strip()}"
)

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# ==========================================
# PROMPT
# ==========================================

def cargar_prompt():

    with open(
        "prompts/prompt_sistema.txt",
        encoding="utf-8"
    ) as f:

        return f.read()


# ==========================================
# IA
# ==========================================

def responder(
    pregunta,
    respuesta_usuario,
    contenido
):

    prompt = cargar_prompt()

    mensaje = f"""

CONTENIDO DEL CURSO

{contenido}

------------------------------------------------

PREGUNTA

{pregunta}

------------------------------------------------

RESPUESTA DEL PARTICIPANTE

{respuesta_usuario}

"""

    respuesta = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        temperature=0.2,

        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": mensaje
            }
        ]

    )

    return respuesta.choices[0].message.content
