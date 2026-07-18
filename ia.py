from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(

    api_key=os.getenv("GROQ_API_KEY"),

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

        model="llama-3.3-70b-versatile",

        temperature=0.2,

        messages=[

            {

                "role":"system",

                "content":prompt

            },

            {

                "role":"user",

                "content":mensaje

            }

        ]

    )

    return respuesta.choices[0].message.content