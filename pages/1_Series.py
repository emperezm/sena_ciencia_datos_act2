import streamlit as st
import pandas as pd

st.title("Método 1: Juntando varias Series")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame agrupando información sobre **películas favoritas**.

1. Crea tres Series de Pandas diferentes:
    - Una serie llamada `titulos` con al menos 4 nombres de películas.
    - Una serie llamada `directores` con los directores de esas películas.
    - Una serie llamada `años` con el año de estreno.
2. Une estas tres series en un único DataFrame llamado `df_peliculas`, asignando nombres descriptivos a las columnas (por ejemplo: `Título`, `Director`, `Año de Estreno`).
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación
titulos = pd.Series(["La vida es bella", "El vestido Rojo", "El niño de la pijama de raya", "Como niños 2"])
directores = pd.Series(["Carmelo", "Rigoberto", "Berenice", "Alfonso"])
años = pd.Series([1970, 2001, 1998, 2010])

df_peliculas= pd.DataFrame ({
    "Titulares" : titulos,
    "Director" : directores,
    "Año de Extreno" :años
})
st.dataframe(df_peliculas)
