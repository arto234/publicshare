import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

st.title("Analyse sur le dataframe des voitures")


regions = df['continent'].unique()
region_map = {" US.": "USA", " Europe.": "Europe", " Japan.": "Japon"}
region = st.radio("Sélectionnez une région :", options=regions, format_func=lambda x: region_map[x])


newdf = df[df['continent'] == region]


st.write(f"🔍 **Données filtrées pour la région : {region_map[region]}**")
st.dataframe(newdf.head())


st.subheader("Matrice de corrélation")


fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(newdf.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
st.pyplot(fig)

st.subheader("Distribution des variables")


variable = st.selectbox("Sélectionnez une variable :", df.columns.drop("continent"))


fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(newdf[variable], bins=20, kde=True, color="royalblue", ax=ax)
plt.xlabel(variable)
plt.title(f"Distribution de {variable} en {region_map[region]}")
st.pyplot(fig)
