import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ==========================================
# 1. CONFIGURACIÓN DE LA PÁGINA Y ESTILOS
# ==========================================
st.set_page_config(
    page_title="Predicción Cardiovascular",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .main-title { font-size: 3rem; color: #C0392B; text-align: center; font-weight: bold; }
    .sub-title { font-size: 1.2rem; text-align: center; color: #7F8C8D; margin-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. CARGA DEL MODELO
# ==========================================
@st.cache_resource
def cargar_modelo():
    try:
        return joblib.load('modelo_pipeline.pkl')
    except Exception as e:
        st.error(f"Error al cargar el modelo. Asegúrate de que 'modelo_pipeline.pkl' esté en la carpeta. Detalle: {e}")
        return None

modelo = cargar_modelo()

# ==========================================
# 3. ENCABEZADO Y PRESENTACIÓN
# ==========================================
st.markdown('<p class="main-title">🫀 Sistema de Predicción Cardiovascular</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Herramienta analítica basada en Machine Learning (Dataset de Cleveland - UCI)</p>', unsafe_allow_html=True)

st.warning("⚠️ **Aviso Importante:** Esta es una aplicación de un prototipo académico. Las predicciones generadas no sustituyen en ningún caso el diagnóstico, consejo o tratamiento de un profesional de la salud.")

with st.expander("Ver Integrantes y Objetivo del Proyecto", expanded=True):
    st.write("""
    **Objetivo:** Desarrollar un modelo predictivo capaz de identificar la probabilidad de presencia de enfermedad cardiovascular basado en variables clínicas y demográficas del paciente.
    
    **Integrantes del Grupo:**
    * Héctor Cervantes Echeverria
    * Juan Guillermo Sarmiento Garrido
    * Santiago Valle Palacio
    * Diego Mendoza Gutiérrez
    """)

# ==========================================
# 4. PESTAÑAS PRINCIPALES (TABS)
# ==========================================
tab1, tab2 = st.tabs(["🩺 Realizar Predicción", "📊 Sobre el Modelo y Entrenamiento"])

# ------------------------------------------
# PESTAÑA 1: FORMULARIO Y PREDICCIÓN
# ------------------------------------------
with tab1:
    if modelo is not None:
        st.markdown("### Ingrese los datos clínicos del paciente")
        
        with st.form("formulario_prediccion"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Datos Demográficos y Básicos**")
                age = st.number_input("Edad (años)", min_value=20, max_value=100, value=50, step=1)
                sex = st.selectbox("Sexo", options=[1, 0], format_func=lambda x: "Hombre" if x == 1 else "Mujer")
                trestbps = st.number_input("Presión arterial en reposo (mm Hg)", min_value=90, max_value=200, value=120)
                chol = st.number_input("Colesterol sérico (mg/dl)", min_value=100, max_value=600, value=200)
                fbs = st.selectbox("Azúcar en sangre en ayunas > 120 mg/dl", options=[0, 1], format_func=lambda x: "Sí" if x == 1 else "No")

            with col2:
                st.markdown("**Datos Clínicos y de Esfuerzo**")
                cp = st.selectbox("Tipo de dolor torácico", options=[1, 2, 3, 4], format_func=lambda x: {1: "Angina Típica", 2: "Angina Atípica", 3: "Dolor no anginoso", 4: "Asintomático"}[x])
                restecg = st.selectbox("Resultados Electrocardiográficos en reposo", options=[0, 1, 2], format_func=lambda x: {0: "Normal", 1: "Anormalidad ST-T", 2: "Hipertrofia ventricular izquierda"}[x])
                thalach = st.number_input("Frecuencia cardíaca máxima alcanzada", min_value=60, max_value=220, value=150)
                exang = st.selectbox("Angina inducida por ejercicio", options=[1, 0], format_func=lambda x: "Sí" if x == 1 else "No")
                oldpeak = st.number_input("Depresión del ST inducida por ejercicio", min_value=0.0, max_value=6.5, value=1.0, step=0.1)

            st.markdown("**Otros Estudios**")
            col3, col4, col5 = st.columns(3)
            with col3:
                slope = st.selectbox("Pendiente del segmento ST", options=[1, 2, 3], format_func=lambda x: {1: "Ascendente", 2: "Plana", 3: "Descendente"}[x])
            with col4:
                ca = st.selectbox("Nº de vasos principales coloreados", options=[0, 1, 2, 3])
            with col5:
                thal = st.selectbox("Talasemia", options=[3, 6, 7], format_func=lambda x: {3: "Normal", 6: "Defecto fijo", 7: "Defecto reversible"}[x])

            st.markdown("<br>", unsafe_allow_html=True)
            submit_button = st.form_submit_button("🔍 Calcular Riesgo Cardiovascular", use_container_width=True)

        # Lógica de predicción individual
        if submit_button:
            datos_paciente = pd.DataFrame([{
                'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps, 'chol': chol,
                'fbs': fbs, 'restecg': restecg, 'thalach': thalach, 'exang': exang,
                'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal
            }])

            prediccion = modelo.predict(datos_paciente)[0]
            probabilidad = modelo.predict_proba(datos_paciente)[0][1]

            st.divider()
            st.markdown("### Resultado del Análisis para este Paciente")
            
            col_res1, col_res2 = st.columns(2)
            with col_res1:
                if prediccion == 1:
                    st.error(f"### 🚨 Alto Riesgo\nEl modelo detecta una **alta probabilidad** de presencia de enfermedad cardiovascular.")
                else:
                    st.success(f"### ✅ Bajo Riesgo\nEl modelo detecta una **baja probabilidad** de presencia de enfermedad cardiovascular.")
            with col_res2:
                st.metric(label="Probabilidad estimada para este paciente", value=f"{probabilidad * 100:.1f} %")
                st.progress(float(probabilidad))

            # Explicación de la predicción individual
            st.info("""
            **¿Qué influyó en este resultado?**
            El modelo de Random Forest evalúa principalmente la Edad, el tipo de dolor torácico (cp), la frecuencia cardíaca máxima (thalach) y la depresión del ST (oldpeak). Según los valores ingresados, el algoritmo calculó esta probabilidad.
            """)

# ------------------------------------------
# PESTAÑA 2: MÉTRICAS Y VISUALIZACIONES DEL ENTRENAMIENTO
# ------------------------------------------
with tab2:
    st.markdown("### Rendimiento del Modelo (Entrenamiento)")
    st.write("El modelo fue entrenado priorizando el **Recall** (sensibilidad), fundamental en contextos médicos para no dejar pasar falsos negativos.")
    
    # Tarjetas de métricas
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Exactitud (Accuracy)", "85.0 %", "Alto")
    m2.metric("Sensibilidad (Recall)", "82.1 %", "Crítico")
    m3.metric("Precisión", "85.1 %")
    m4.metric("F1-Score", "83.6 %")

    st.divider()
    
       # Imágenes del Entrenamiento juntas
    st.markdown("### Evaluación Gráfica del Entrenamiento")
    col_img1, col_img2 = st.columns(2)
    
    with col_img1:
        st.markdown("#### Matriz de Confusión")
        try:
            # Usamos la ruta de la carpeta imagenes/
            st.image("top_variables.png", caption="Matriz de Confusión - Random Forest", use_container_width=True)
        except:
            st.warning("Falta la imagen 'top_variables.png' en la carpeta 'imagenes'.")

    with col_img2:
        st.markdown("#### Top 10 Variables más Importantes")
        try:
            # Usamos la ruta de la carpeta imagenes/
            st.image("matriz_confusion.png", caption="Importancia de las variables clínicas", use_container_width=True)
        except:
            st.warning("Falta la imagen 'matriz_confusion.png' en la carpeta 'imagenes'.")

    st.divider()
    st.markdown("### Limitaciones del Modelo")
    st.info("""
    * **Tamaño de la muestra:** Entrenado con 297 registros limpios (Dataset de Cleveland). Un mayor volumen de datos mejoraría la generalización.
    * **Datos de entrada:** El modelo depende enteramente de la exactitud de los exámenes médicos ingresados.
    * **Uso restringido:** Esta herramienta es un ejercicio académico y no está certificada para uso clínico real.
    """)
