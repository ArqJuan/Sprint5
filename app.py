import streamlit as st 
import pandas as pd 
import plotly_express as px 

car_data = pd.read_csv('/Users/user/Desktop/Repositories/Sprint5/vehicles_us.csv')

#para ver que funciono importar el archivo CSV
print(car_data.head(20))

#Exit para cerrar el ambiente del codigo en la terminal, no tocar o caera Roma
#Segun un post encontrado en StackOverflow



hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    
if hist_button:
    st.write('Creacion de grafico de disperion')
    fig = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(fig, use_container_width=True)

build_hist = st.checkbox('Construir un histograma')
if build_hist: # al hacer clic en el botón
    
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    
if build_hist:
    st.write('Creacion de grafico de disperion')
    fig = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(fig, use_container_width=True)




exit()