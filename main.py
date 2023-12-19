import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Weather Forcast for the Next Days")

place = st.text_input("place",placeholder="Enter Your City Name")

Days = st.slider("Forcast Days",min_value=1,max_value=5,
                 help="Select The Number of Forcast Days")

option = st.selectbox("Select the data to view",
                      ("Temperature","Sky"),)

st.subheader(f"{option} for the next {Days} days in {place}")

def get_data(Days):
    dates = ["2023-25-10", "2023-26-10", "2023-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [Days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(Days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)





