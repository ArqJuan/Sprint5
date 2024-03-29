import streamlit as st 
import pandas as pd 
import plotly_express as px 

car_data = pd.read_csv('vehicles_us.csv')

#para ver que funciono importar el archivo CSV
print(car_data.head(20))

#Exit para cerrar el ambiente del codigo en la terminal, no tocar o caera Roma
#Segun un post encontrado en StackOverflow

st.title('Creacion de Histrogramas')
st.subheader('Lectura de archivo vehicle_us.csv', divider='blue')

#Creacion de 2 Histogramas
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    
    st.subheader('Cantidad de carros por Kilometraje')
    st.write('Histograma Kilometraje')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    st.write('En este grafico se muestra la cantidad de carros en venta por kilometraje para poder tener una relacion general del uso previo a la venta')
    
if hist_button:
    st.subheader('Precio VS Kilometraje')
    st.write('Grafico de dispersion Precio VS Kilometraje')
    fig = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(fig, use_container_width=True)
    st.write('En este grafico nos enfocamos en el precio contra el kilometraje para determinar si el kilometraje es un factor fuerte en los precios')


#Creacion checkbox de Histograma
build_hist = st.checkbox('Construir un histograma')
if build_hist: # al hacer clic en el botón
    
    st.subheader('Cuantos y que modelos hay?')
    st.write('Histograma Cantidad por Modelos')
    fig = px.histogram(car_data, x="model")
    st.plotly_chart(fig, use_container_width=True)
    st.write('En este grafico se muestra la cantidad de carros a la venta por cada modelo en nuestra base de datos.')


#creacion de checkbox para Grafica de Dispersion
build_hist = st.checkbox('Construir una Grafica de dispersion')    
if build_hist:
    
    st.subheader('A~no vs Precio')
    st.write('Creacion de grafico de disperion')
    fig = px.scatter(car_data, x = 'model_year', y = 'price')
    st.plotly_chart(fig, use_container_width=True)
    st.write(f'En este grafico estamos comparando el precio de venta contra el modelo del vehiculo. normalmente el libro azul impacta el precio final n/por lo que deberia de haber una correlacion fuerte.')




exit()
