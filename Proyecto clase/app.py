import streamlit as st 
import pandas as pd 

st.header('Estado de la Prestación del servicio')
st.subheader('Zonas no Interconectadas de Energía')
st.text('Conjunto de Datos')

ruta = 'data/Estado_de_la_prestación_del_servicio_de_energía_en_Zonas_No_Interconectadas_20260422.csv'
df = pd.read_csv(ruta)

st.dataframe(df)

## ANALISIS DE DATOS 

filas = df.shape[0]
columnas = df.shape[1]

## VISUALIZACIÓN DE DATOS 

col1, col2 = st.columns(2)

## Indicadores en dos columnas 
with col1:
    with st.container(border=True): 
        st.text('Numero de filas')
        st.subheader(filas)

with col2:
    with st.container(border=True): 
        st.text('Numero de Columnas')
        st.subheader(columnas)


## Otra forma de mostrar los indicadores
col3, col4 = st.columns(2)
with col3: 
    st.metric('numero de filas', filas, border=True)
with col4:
    st.metric('Numero de columnas', columnas, border=True)


print('Hello World')
