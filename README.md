# 🚗 Predicción de Precios de Vehículos con Machine Learning

## 📌 Resumen
Este proyecto consiste en el desarrollo de una aplicación web interactiva construida con **Streamlit**, cuyo objetivo es permitir a los usuarios ingresar características de un vehículo para **predecir su precio en dólares**, utilizando un **modelo de machine learning previamente entrenado**.  
La aplicación se enfoca en la facilidad de uso y en la eficiencia, evitando el reentrenamiento del modelo y ofreciendo resultados inmediatos.

---

## 🧠 Descripción del Proyecto
El sistema permite al usuario ingresar datos relevantes del vehículo como el fabricante, tipo de motor, tipo de combustible, año y kilometraje.  
Estos datos son procesados y enviados a un modelo de regresión entrenado previamente, el cual devuelve una estimación del precio del vehículo.

El proyecto está pensado como una solución práctica para demostrar la aplicación de modelos de machine learning en un entorno real y accesible para el usuario final.

---

## 📊 Modelo de Machine Learning
- **Tipo de problema:** Regresión
- **Variable objetivo:** Precio del vehículo (USD)
- **Variables de entrada:**
  - Fabricante
  - Motor
  - Combustible
  - Año
  - Kilometraje
- **Librerías utilizadas:** Scikit-learn, Pandas, NumPy
- **Modelo cargado:** Modelo previamente entrenado usando `joblib`

---

## 🖥️ Aplicación Web con Streamlit
La aplicación web fue desarrollada con [Streamlit] (https://predictcarpriceapp-3d6jxfsgnklqzlvcn8q8ih.streamlit.app/) y cuenta con:
- Inputs interactivos para el ingreso de datos
- Botón para generar la predicción
- Conversión del resultado final a dólares
- Carga del modelo sin necesidad de reentrenarlo
- Interfaz sencilla e intuitiva para el usuario

---


