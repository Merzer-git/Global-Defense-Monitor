import streamlit as st

st.set_page_config(
    page_title= "Global Defense Monitor",
    page_icon= "🌎",
    layout= "wide"
)

st.title("🌎 Global Defense Monitor")
st.subheader("La Guerra en números: 75 años de Gasto Militar")

st.markdown("""
    **Este dashboard explora la evoluciÓn en el Gasto Militar a nivel global, regional y por países.** Se analizan datos históricos de partidas presupuestarias destinadas a defensa recolectadas por el **SIPRI** (1949 - 2024) complementada con datos del **Banco Mundial** para entender las dinámicas de rearme, hegemonía y los conflictos geopolíticos que moldearon el mundo moderno.
""")
st.divider()

with st.expander("Contexto Histórico: De la Guerra Fría a la actualidad"):
    st.markdown(
    """
    **El Legado de la Guerra Fría**:
    Tras la finalización de la Segunda Guerra Mundial el escenario global entró en un periodo histórico donde los máximos exponentes de la victoria frente a las Potencias del Eje, **Estados Unidos** y la **Unión de Repúblicas Socialistas Soviéticas**, se vieron enfrentados en una confrontación geopolítica atípica: una guerra ideológica. Este periodo, conocido como Guerra Fría, sentó un precedente peligroso para la historia moderna de los países: la "tensa calma".

    **La Amenaza Nuclear**:
    Durante décadas, el mundo estuvo al borde de un conflicto global sin precedentes, donde un error diplomático, un fallo de cálculo en una prueba nuclear o una escalada militar accidental podrían haber sido detonantes catastróficos. En este contexto, se registraron aumentos sustanciales en los presupuestos de defensa, los cuales, en determinadas potencias, fueron destinados a financiar la investigación y desarrollo de armas de destrucción masiva.

    **El Nuevo Orden Mundial**:
    La disolución de la URSS el 26 de diciembre de 1991, tras una serie de complejas reestructuraciones políticas y económicas, marcó el fin formal de este periodo. No obstante, la herencia de esta "paz armada" y la lógica de disuasión estratégica continúan influyendo, hasta el día de hoy, en las planificaciones militares de las naciones soberanas.
    """
)

st.info("**Selecciona una página del menu lateral**")

st.markdown("""
    <style>
        /* Reduce el padding superior del contenedor principal */
        .block-container {
            padding-top: 3rem;
            padding-bottom: 0rem;
            margin-top: 0rem;
        }
        
        /* Opcional: Ocultar el menú de hamburguesa y el footer de 'Made with Streamlit' 
           (Recomendado solo para el producto final) */
        
        /* #MainMenu {visibility: hidden;} */
        /* footer {visibility: hidden;} */
        
    </style>
""", unsafe_allow_html=True)