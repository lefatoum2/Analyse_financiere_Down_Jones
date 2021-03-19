import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import mysql.connector


# Titre et image
st.title("Down Jones")
image = Image.open('./michael.jfif')
st.markdown("Pour calculer le Dow Jones, la somme des prix des 30 actions est divisée par un diviseur, le Dow Divisor. Le diviseur est ajusté en cas de fractionnement d'actions, de scission ou de changements structurels similaires, pour s'assurer que de tels événements ne modifient pas en eux-mêmes la valeur numérique du Dow Jones. Au début, le diviseur initial était composé du nombre initial de sociétés de composants; cela a d'abord fait du Dow Jones une simple moyenne arithmétique.")
st.image(image)

# Data
# data1 = pd.read_csv("trade5.csv")
config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'port': '3300',
    'database': 'jones',
    'raise_on_warnings': True,
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()
# recuperation de la liste apprenant à partir de la base de donnees
cursor.execute("""select * from trade5 """)
# creation d'un tableau avec la liste des apprenants
dataun = cursor.fetchall()
data1 = pd.DataFrame(dataun)
data1.columns = ["Index", "Annee", "Closing value", "Change in points", "Change in percent"]


# Selection
# symbols = data1.columns.sort_values().tolist()
sy = ["Closing value", "Change in points","Change in percent"]
ticker = st.sidebar.selectbox(
    'Choisir une valeur',
    sy)

# Affichage de la data
st.dataframe(data1.loc[:, ['Annee', ticker]])


# Affichage des graphiques
fig = go.Figure(data=go.Scatter(x=data1['Annee'], y=data1['Closing value']))

fig.update_layout(
    title={
        'text': "Valeur du Down Jones à la fermeture selon l'année",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
st.plotly_chart(fig, use_container_width=True)

fig = go.Figure(data=go.Scatter(x=data1['Annee'], y=data1['Change in points']))

fig.update_layout(
    title={
        'text': "Nombre de points du Down Jones à l'année",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
st.plotly_chart(fig, use_container_width=True)

fig = go.Figure(data=go.Scatter(x=data1['Annee'], y=data1['Change in percent']))

fig.update_layout(
    title={
        'text': "Change en pourcentage du Down Jones à l'année",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
st.plotly_chart(fig, use_container_width=True)
