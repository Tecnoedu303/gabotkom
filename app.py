import streamlit as st

from gabotkom import GaBotKom


# =====================================
# CONFIGURACIÓN
# =====================================

st.set_page_config(
    page_title="GaBotKom",
    page_icon="🤖",
    layout="wide"
)


# =====================================
# SESSION STATE
# =====================================

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "nombre" not in st.session_state:
    st.session_state.nombre = ""

if "empresa" not in st.session_state:
    st.session_state.empresa = "Komatsu"

if "bot" not in st.session_state:
    st.session_state.bot = GaBotKom()


bot = st.session_state.bot


# =====================================
# CABECERA
# =====================================

# =====================================
# CABECERA
# =====================================

st.title("🤖 GaBotKom")
st.subheader("Plataforma Inteligente de Capacitación Corporativa")
st.divider()


# =====================================
# PANTALLA INICIAL
# =====================================

if st.session_state.pantalla == "inicio":

    st.markdown("## Bienvenido")

    st.write(
        "Esta plataforma adapta la capacitación al nivel de conocimientos del participante."
    )

    nombre = st.text_input(
        "Nombre del participante"
    )

    empresa = st.text_input(
        "Empresa",
        value="Komatsu"
    )

    if st.button("Iniciar capacitación"):

        st.session_state.nombre = nombre
        st.session_state.empresa = empresa
        st.session_state.pantalla = "curso"

        st.rerun()


# =====================================
# CURSO
# =====================================

elif st.session_state.pantalla == "curso":

    st.progress(bot.progreso())

    col1, col2 = st.columns([3,1])

    with col1:

        st.write(f"### 👤 {st.session_state.nombre}")
        st.write(f"🏢 {st.session_state.empresa}")
        st.write(f"📚 {bot.curso}")
        st.write(f"📖 Tema: {bot.tema}")

    with col2:

        st.metric(
            "Lección",
            f"{bot.numero_leccion} / {bot.total_lecciones}"
        )

    st.divider()

    st.markdown(bot.leccion)

    try:
        from curso import obtener_imagen

        st.image(
            str(obtener_imagen()),
            use_container_width=True
        )
    except:
        pass

    st.divider()

    st.subheader("Conversación")
        # =====================================
    # HISTORIAL
    # =====================================

    historial = bot.obtener_historial()

    for mensaje in historial:

        rol = "assistant"

        if mensaje["rol"] == "usuario":
            rol = "user"

        with st.chat_message(rol):
            st.markdown(
                mensaje["mensaje"]
            )

    # =====================================
    # CHAT
    # =====================================

    pregunta = st.chat_input(
        "Escribe tu pregunta..."
    )

    if pregunta:

        # Mostrar inmediatamente el mensaje del usuario

        with st.chat_message("user"):
            st.markdown(pregunta)

        with st.spinner(
            "🤖 GaBotKom está analizando tu respuesta..."
        ):

            respuesta = bot.conversar(
                pregunta
            )

        st.rerun()

    # =====================================
    # SIDEBAR
    # =====================================

    with st.sidebar:

        st.header("GaBotKom")

        st.write(
            f"**Curso:** {bot.curso}"
        )

        st.write(
            f"**Tema:** {bot.tema}"
        )

        st.write(
            f"**Lección:** {bot.numero_leccion}/{bot.total_lecciones}"
        )

        st.progress(
            bot.progreso()
        )

        st.divider()

        if st.button("🔄 Reiniciar conversación"):

            st.session_state.bot = GaBotKom()

            st.rerun()

        st.divider()

        st.caption(
            "GaBotKom MVP v0.1\nKomatsu Training Center"
        )