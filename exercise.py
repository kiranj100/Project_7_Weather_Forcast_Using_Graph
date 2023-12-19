import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search of Happiness")

x_axis = st.selectbox("Select the Data from x-axis",("GDP","Hapiness","Generosity"))

y_axis = st.selectbox("Select the Data from y-axis",("GDP","Happiness","Generosity"))

df = pd.read_csv("happy.csv")

x_array = None
match x_axis:
    case "GDP":
        x_array = df['gdp']
    case "Happiness":
        x_array = df['happiness']
    case "Generosity":
        x_array = df['generosity']

y_array = None
match y_axis:
    case "GDP":
        y_array = df['gdp']
    case "Happiness":
        y_array = df['happiness']
    case "Generosity":
        y_array = df['generosity']

st.subheader(f"{x_axis} and {y_axis}")

figure1 = px.scatter(y=y_array, x=x_array, labels={"x":"x_axis","y":"y_axis"})

st.plotly_chart(figure1)



