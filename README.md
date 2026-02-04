# 🚗 Predicción de Precios de Vehículos con Machine Learning

## 📌 Resumen


Este proyecto consiste en el desarrollo de una aplicación web interactiva construida con Streamlit, cuyo objetivo es permitir a los usuarios ingresar características de un vehículo para predecir su precio en dólares, utilizando un modelo de machine learning previamente entrenado.
La aplicación se enfoca en la facilidad de uso y en la eficiencia, evitando el reentrenamiento del modelo y ofreciendo resultados inmediatos.


| Variable           | Descripción             | Ejemplo                              |
| ------------------ | ----------------------- | ------------------------------------ |
| `fabricante`       | Marca del vehículo      | Toyota, Ford, BMW                    |
| `tipo_motor`       | Configuración del motor | V4, V6, V8, Eléctrico                |
| `tipo_combustible` | Combustible utilizado   | Gasolina, Diésel, Híbrido, Eléctrico |
| `año`              | Año de fabricación      | 2015, 2020, 2023                     |
| `kilometraje`      | Millas recorridas       | 25000, 80000                         |

---

## 🧠 Descripción del Proyecto
Sistema de screening diabético basado en SVM que procesa 8 biomarcadores clínicos vía CSV para clasificar riesgo (Bajo/Alto) en segundos, sin reentrenamiento, con 95.7% de sensibilidad. Solución práctica de ML para atención primaria.

---

## 📊 Modelo de Machine Learning

Se centra en el desarrollo de una aplicación web amigable e interactiva mediante el uso de Streamlit, con el propósito de facilitar la interacción del usuario final con el modelo de Machine Learning. La aplicación permite el ingreso de nuevos datos de forma estructurada e intuitiva para realizar predicciones de precio en tiempo real. En esta fase se carga el modelo previamente entrenado y serializado, junto con su pipeline de preprocesamiento, evitando la necesidad de reentrenamiento y asegurando consistencia entre el entorno de desarrollo y el de producción. Este enfoque permite demostrar la viabilidad del modelo en un escenario práctico, así como su capacidad de generalización al aplicarse sobre datos no vistos.

---

## 🖥️ Aplicación Web con Streamlit

La aplicación web fue desarrollada con [Streamlit App](https://predictcarpriceapp-3d6jxfsgnklqzlvcn8q8ih.streamlit.app/)  y cuenta con:
* Formulario interactivo para ingreso manual de datos del vehículo (5 características: fabricante, tipo de motor, tipo de combustible, año y kilometraje).
* Botón para generar la predicción del precio en dólares.
* Visualización del resultado con el precio estimado y nivel de confianza del modelo.
* Carga del modelo de regresión sin necesidad de reentrenarlo.
* Interfaz sencilla e intuitiva optimizada para compradores y vendedores de vehículos usados.

---


