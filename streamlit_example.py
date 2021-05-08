import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.write("""
# My first app
Hello *world!*
""")

df = pd.read_csv("world_cup_2018_squads.csv",encoding='iso-8859-1')
st.line_chart(df['Caps'])