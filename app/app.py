import pandas as pd
import numpy as np
import joblib
import streamlit as st
import sklearn  

@st.cache_resource
def load_model():
    return joblib.load('model2.pkl') 

model =  load_model()


st.title("Predicción de precio de automóvil")

st.subheader("Ingrese las características del vehículo")

# ─── Inputs categóricos ──────────────────────────────
fabricante = st.selectbox(
    "Fabricante",
    options=["Toyota", "VW", "Ford", "BMW", "Porshe"]
        
)

combustible = st.selectbox(
    "Tipo de combustible",
    options=["Petrol", "Diesel", "Hybrid"]
)

# ─── Inputs numéricos ──────────────────────────────
motor = st.number_input(
    "Motor",
    min_value=0.8,
    max_value=8.0,
    step=0.1,
    value=1.8
)

año = st.number_input(
    "Año",
    min_value=1990,
    max_value=2025,
    step=1,
    value=2018
)

kilometraje = st.number_input(
    "Kilometraje",
    min_value=0,
    max_value=500_000,
    step=1_000,
    value=60_000
)

input_df = pd.DataFrame(
       {
          'Fabricante':[fabricante],
          'Motor':[motor],
          'Combustible':[combustible],
          'Año':[año],
          'Kilometraje':[kilometraje]
      }
)

st.subheader("Datos de entrada")
st.dataframe(input_df)

def Predict(x):
    pred = model.predict(x)

    return np.round(pred,2)


if st.button('Predecir precio'):
    
    pred = Predict(input_df)
    st.text(f"Valor estimado en dólares: {pred}")
    





