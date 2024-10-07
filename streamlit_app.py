from sqlite3 import SQLITE_BUSY_RECOVERY
import streamlit as st

st.title("🌱 TouriSieve")
st.write(
    "bonjour, voici un questionnaire sur les fuites économiques :")

st.write("Aimez-vous les lasagnes ?")
survey.radio("Likert scale:", options=["NA", "😞", "🙁", "😐", "🙂", "😀"], horizontal=True)

