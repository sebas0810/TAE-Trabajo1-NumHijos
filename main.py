import streamlit as st
import pandas as pd
import math
from pycaret.regression import *

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def cargarModelo():
  return load_model('./modelo/model_pre_clas')

res = []

df_model = cargarModelo()
st.title('Número de Hijos en el Hogar')
st.subheader('Video de la Aplicación')
st.video('https://www.youtube.com/watch?v=uWK5PUt7Gag')

st.sidebar.warning('Si no hay un padre o una madre en el hogar, por favor no modificar los campos de entrada correspondientes a este.')

# PADRE
st.sidebar.header('Datos de Entrada del Padre')
st.subheader("Descripción de las Preguntas Relacionadas al Padre")

edadPadre = st.sidebar.number_input('1. Edad del padre (años)', 0, 100, 0, 1)
st.markdown("1. Edad del padre (años)")
res.append(edadPadre)

nivEducativoPadre = st.sidebar.number_input('2. ¿Cuál es el nivel educativo más alto alcanzado por el padre y el último año o grado aprobado en este nivel?', 0, 13, 0, 1)
st.markdown("""2. ¿Cuál es el nivel educativo más alto alcanzado por el **padre** y el último año o grado aprobado en este nivel?""")
st.text("""1: Ninguno
2: Preescolar
3: Básica Primaria (1º - 5º)
4: Básica secundaria (6º--9º)
5: Media (10º--13º)
6: Técnico sin título
7: Técnico con título
8: Tecnológico sin título
9: Tecnológico con título
10: Universitario sin titulo
11: Universitario con titulo
12: Postgrado sin titulo
13: Postgrado con titulo""") 
res.append(nivEducativoPadre)

actPadre = st.sidebar.slider('4. ¿En que actividad ocupó el padre la mayor parte del tiempo LA SEMANA PASADA?', 1, 6, 1, 1)
st.markdown("4. ¿En que actividad ocupó el **padre** la mayor parte del tiempo LA SEMANA PASADA?")
st.text("""1 Trabajando
2 Buscando trabajo
3 Estudiando
4 Oficios del hogar
5 Incapacitado permanentemente para trabajar
6 Otra actividad ¿cuál? """)
res.append(actPadre)

tipoContratoPadre = st.sidebar.slider('5. ¿El contrato de trabajo del **padre** es a termino indefinido o a termino fijo?', 0, 2, 0, 1)
st.markdown("5. ¿El contrato de trabajo del padre es a termino indefinido o a termino fijo?")
st.text("""0 Ningún contrato
1 A termino Indefinido
2 A termino fijo """)
res.append(tipoContratoPadre)

# MADRE
st.sidebar.header('Datos de Entrada de la Madre')
st.subheader("Descripción de las Preguntas Relacionadas a la Madre")

edadMadre = st.sidebar.number_input('1. Edad de la madre (años)', 0, 100, 0, 1)
st.markdown("1. Edad de la madre (años)")
res.append(edadMadre)

nivEducativoMadre = st.sidebar.number_input('2. ¿Cuál es el nivel educativo más alto alcanzado por la madre y el último año o grado aprobado en este nivel?', 0, 13, 0, 1)
st.markdown("""2. ¿Cuál es el nivel educativo más alto alcanzado por la **madre** y el último año o grado aprobado en este nivel?""")
st.text("""1: Ninguno
2: Preescolar
3: Básica Primaria (1º - 5º)
4: Básica secundaria (6º--9º)
5: Media (10º--13º)
6: Técnico sin título
7: Técnico con título
8: Tecnológico sin título
9: Tecnológico con título
10: Universitario sin titulo
11: Universitario con titulo
12: Postgrado sin titulo
13: Postgrado con titulo""") 
res.append(nivEducativoMadre)

actMadre = st.sidebar.slider('4. ¿En que actividad ocupó el madre la mayor parte del tiempo LA SEMANA PASADA?', 1, 6, 1, 1)
st.markdown("4. ¿En que actividad ocupó la **madre** la mayor parte del tiempo LA SEMANA PASADA?")
st.text("""1 Trabajando
2 Buscando trabajo
3 Estudiando
4 Oficios del hogar
5 Incapacitado permanentemente para trabajar
6 Otra actividad ¿cuál? """)
res.append(actMadre)

tipoContratoMadre = st.sidebar.slider('5. ¿El contrato de trabajo de la **madre** es a termino indefinido o a termino fijo?', 0, 2, 0, 1)
st.markdown("5. ¿El contrato de trabajo de la madre es a termino indefinido o a termino fijo?")
st.text("""0 Ningún contrato
1 A termino Indefinido
2 A termino fijo """)
res.append(tipoContratoMadre)

st.sidebar.header('Datos de Vivienda')
st.subheader("Descripción de las Preguntas Relacionadas a la Vivienda")

region = st.sidebar.slider('1. Región', 1, 9, 1, 1)
st.markdown("1. Región")
st.text("""1 Caribe
2 Oriental
3 Central
4 Pacífica(sin valle)
5 Bogotá
6 Antioquia
7 Valle del cauca
8 San Andrés
9 Orinoquía - amazonía """)
res.append(region)

cantidadHogares = st.sidebar.number_input('2. Cantidad de hogares en la vivienda', 0, 10, 0, 1)
st.markdown("""2. Cantidad de hogares en la vivienda """)
res.append(cantidadHogares)

clase = st.sidebar.slider('3. Clase', 1, 2, 1, 1)
st.markdown("3. Clase")
st.text("""1 Cabecera
2 Centros poblados, inspección de policía o corregimientos - Área rural dispersa """)
res.append(clase)

tipoVivienda = st.sidebar.slider('4. Tipo de vivienda', 1, 5, 1, 1)
st.markdown("4. Tipo de vivienda")
st.text("""1 Casa
2 Apartamento
3 Cuarto(s)
4 Vivienda tradicional indigena
5 Otro (carpa, contenedor, vagón, embarcación, cueva, refugio natural, etc) """)
res.append(tipoVivienda)

energia = st.sidebar.slider('5. ¿Cuenta la vivienda con el servico de energía eléctrica?', 1, 2, 1, 1)
st.markdown("5. ¿Cuenta la vivienda con el servico de energía eléctrica?")
st.text("""1 Sí
2 No """)
res.append(energia)

valTarifaElec = st.sidebar.slider('6. Según su estrato cuál es el valor de la tarifa eléctrica', 1, 9, 1, 1)
st.markdown("6. Según su estrato cuál es el valor de la tarifa eléctrica")
st.text("""1 Bajo - Bajo
2 Bajo
3 Medio - Bajo
4 Medio
5 Medio - Alto
6 Alto
8 Planta eléctrica
9 No conoce el estrato o no cuenta con recibo de pago.
0 Recibos sin estrato o el servicio es pirata """)
res.append(valTarifaElec)

acueducto = st.sidebar.slider('7. ¿Cuenta la vivienda con el servico de acueducto?', 1, 2, 1, 1)
st.markdown("7. ¿Cuenta la vivienda con el servico de acueducto?")
st.text("""1 Sí
2 No """)
res.append(acueducto)

alcantarillado = st.sidebar.slider('8. ¿Cuenta la vivienda con el servico de alcantarillado?', 1, 2, 1, 1)
st.markdown("8. ¿Cuenta la vivienda con el servico de alcantarillado?")
st.text("""1 Sí
2 No """)
res.append(alcantarillado)

st.sidebar.header('Servicios del Hogar')
st.subheader("Descripción de las Preguntas Relacionadas a los Servicios del Hogar")

ingresosHogar = st.sidebar.number_input('1. Ingreso Mensual Total del Hogar', 0, 100000000, 0, 1)
st.markdown("1. Ingreso Mensual Total del Hogar")
res.append(ingresosHogar)

numCuartos = st.sidebar.number_input('2. Incluyendo sala y comedor, ¿de cuántos cuartos o piezas dispone este hogar ?', 1, 20, 1, 1)
st.markdown("2. Incluyendo sala y comedor, ¿de cuántos cuartos o piezas dispone este hogar ?")
res.append(numCuartos)

numPersonasHogar = st.sidebar.number_input('3. Cantidad de personas en el hogar', 1, 20, 1, 1)
st.markdown('3. Cantidad de personas en el hogar')
res.append(numPersonasHogar)

sent = st.sidebar.button('Predecir número de hijos')
indi = ['EDAD_PADRE', 'P8587_PADRE', 'P6240_PADRE', 'P6460_PADRE', 'EDAD_MADRE', 'P8587_MADRE', 'P6240_MADRE', 'P6460_MADRE', 
'REGION', 'CANT_HOGARES_VIVIENDA', 'CLASE', 'P1070','P8520S1', 'P8520S1A1', 'P8520S5', 'P8520S3', 'I_HOGAR','P5000','CANT_PERSONAS_HOGAR']
aux = pd.DataFrame([res], columns=indi)
#st.dataframe(aux)


if(sent):
  st.header("RESULTADO")
  result = df_model.predict(aux)
  st.balloons()
  if(edadMadre == 0 and edadPadre == 0):
    st.success('El numero de hijos(🧒) en el hogar es : '+str(0))
  elif(result == numPersonasHogar):
    if(numPersonasHogar==1): 
      st.success('El numero de hijos(🧒) en el hogar es : '+str(0))
    else: 
      st.success('El numero de hijos(🧒) en el hogar es : '+str((result-2)))
  else:
    st.success('El numero de hijos(🧒) en el hogar es : '+str(result))

st.subheader('Realizado por:')
st.markdown("""Edhy Santiago Marín Arbeláez \n
Sebastián López restrepo \n
Valentín de la Rosa Rueda \n
Juan José Martínez Posada \n
David González Jiménez""")