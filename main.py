import streamlit as st

st.set_page_config(layout="wide")

st.title("Weather Forcast for the Next Days")

place = st.text_input("place",placeholder="Enter Your City Name")

Days = st.slider("Forcast Days",min_value=1,max_value=5,
                 help="Select The Number of Forcast Days")

option = st.selectbox("Select the data to view",
                      ("Temperature","Sky"),)

st.subheader(f"{option} for the next {Days} days in {place}")




