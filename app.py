import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🏎 Formula One Live Tracker")

# Upload datasets
circuits = pd.read_csv("circuits.csv")
constructors = pd.read_csv("constructors.csv")
constructor_standings = pd.read_csv("constructor_standings.csv")
driver_standings = pd.read_csv("driver_standings.csv")

st.header("Driver Standings")

st.dataframe(driver_standings.head(10))

# Driver Points Graph
st.subheader("Top Driver Points")

top_drivers = driver_standings.sort_values(
    by='points',
    ascending=False
).head(10)

fig, ax = plt.subplots(figsize=(10,5))

sns.barplot(
    x='position',
    y='points',
    data=top_drivers,
    ax=ax
)

st.pyplot(fig)

# Constructor Standings
st.header("Constructor Standings")

top_teams = constructor_standings.sort_values(
    by='points',
    ascending=False
).head(10)

st.dataframe(top_teams)

fig2, ax2 = plt.subplots(figsize=(10,5))

sns.barplot(
    x='position',
    y='points',
    data=top_teams,
    ax=ax2
)

st.pyplot(fig2)

# Circuit Analysis
st.header("Circuit Analysis")

country_count = circuits['country'].value_counts().head(10)

fig3, ax3 = plt.subplots(figsize=(10,5))

country_count.plot(kind='bar', ax=ax3)

st.pyplot(fig3)

st.success("Formula One Live Tracker Running Successfully!")
