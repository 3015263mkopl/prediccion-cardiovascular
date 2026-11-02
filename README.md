
# Predicción de Enfermedades Cardiovasculares

## Descripción del proyecto

Este proyecto corresponde a la asignatura de Minería de Datos de la Universidad de la Costa.

Su objetivo es desarrollar una aplicación web interactiva que permita estimar la presencia de enfermedades cardiovasculares a partir de variables clínicas del conjunto de datos Cleveland de UCI.

Para realizar las predicciones se utiliza un modelo de clasificación Random Forest optimizado mediante GridSearchCV. El modelo incluye un pipeline de preprocesamiento con StandardScaler para variables numéricas y OneHotEncoder para variables categóricas.

La aplicación fue desarrollada utilizando Python y Streamlit, y se encuentra desplegada mediante Streamlit Community Cloud.

## Integrantes

- Diego Mendoza Gutierrez
- Héctor Cervantes Echeverria
- Juan Guillermo Sarmiento Garrido
- Santiago Valle Palacio

## Tecnologías utilizadas

- Python
- Pandas
- Scikit-learn
- Random Forest
- GridSearchCV
- Joblib
- Streamlit
- GitHub

## Fuente de datos

UCI Machine Learning Repository.

Dataset: Heart Disease Dataset - Cleveland.

https://archive.ics.uci.edu/dataset/45/heart+disease

## Características del modelo

Variable objetivo:

- target = 0: Sin enfermedad
- target = 1: Enfermedad cardiovascular

Variables de entrada:

- age
- sex
- cp
- trestbps
- chol
- fbs
- restecg
- thalach
- exang
- oldpeak
- slope
- ca
- thal

## Métricas de evaluación

| Métrica | Resultado |
|---|---|
| Accuracy | 0.85 |
| Recall | 0.82 |
| F1-Score | 0.84 |
| ROC-AUC | 0.91 |

Los resultados corresponden a la evaluación del modelo
realizada durante el desarrollo del proyecto.

## Cómo ejecutar localmente

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Entrar a la carpeta

```bash
cd prediccion-cardiovascular
```

### 3. Crear el entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá en el navegador,
normalmente en http://localhost:8501.

## Evaluación del uso de IA

### Herramienta utilizada

ChatGPT, desarrollado por OpenAI.

### Propósito

La inteligencia artificial fue utilizada como herramienta
de apoyo para estructurar y desarrollar la aplicación
web en Streamlit, organizar los componentes de la
interfaz y documentar el proceso de despliegue.

### Prompt principal

Actúa como un ingeniero de Machine Learning y
desarrollador experto en Streamlit.

Ayúdame a integrar un pipeline de clasificación
Random Forest optimizado mediante GridSearchCV,
entrenado con el dataset Cleveland de UCI, en una
aplicación web interactiva.

La aplicación debe permitir ingresar las variables
clínicas, realizar predicciones, mostrar probabilidades,
presentar métricas de evaluación y desplegarse mediante
GitHub y Streamlit Community Cloud.

### Cómo se verificó la respuesta

El código generado fue revisado y ejecutado en el
entorno local.

Se comprobó la carga del pipeline, el funcionamiento
del formulario y la generación de predicciones.

Las predicciones de la aplicación se compararon con
las obtenidas en el notebook para los mismos registros.

También se verificó el funcionamiento de la aplicación
después de su despliegue en Streamlit Community Cloud.

### Problemas encontrados

- Posibles diferencias entre las versiones de las
  librerías utilizadas localmente y en la nube.
- Necesidad de mantener el orden y los nombres
  originales de las variables del modelo.
- Posibles errores en la carga del archivo serializado.
- Ajustes necesarios en la interfaz y validación
  de los datos ingresados.

### Ajustes realizados

- Se organizó el código en secciones.
- Se incorporó la carga del pipeline mediante joblib.
- Se implementó un formulario interactivo.
- Se añadieron validaciones de entrada.
- Se incorporaron métricas y visualizaciones.
- Se revisó la compatibilidad de las dependencias.
- Se verificó la correspondencia entre las predicciones
  del notebook y las de Streamlit.

## Limitaciones

La aplicación es un prototipo académico y no sustituye
la valoración de un profesional de la salud.

El rendimiento depende de la calidad de los datos
ingresados y de las características de la muestra
utilizada para entrenar el modelo.

## Licencia y uso

Proyecto académico desarrollado con fines educativos.
# prediccion-cardiovascular
