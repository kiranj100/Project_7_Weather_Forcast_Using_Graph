import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text_input, slider, select_box, sub_header
st.title("Weather Forcast for the Next Days")

place = st.text_input("place", placeholder="Enter Your City Name")

Days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select The Number of Forcast Days")

option = st.selectbox("Select the data to view",
                      ("Temperature", "Sky"), )

st.subheader(f"{option} for the next {Days} days in {place}")

# if place is empty then nothing happen
if place:
    try:
        # Get the Temperature and Sky Data
        filtered_data = get_data(place, Days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"] / 10 for dict in filtered_data]
            datas = [dict['dt_txt'] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=datas, y=(temperature) ,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            # String wise images set by Weather
            images = {"Clear":"images/clear.png","Clouds":"images/cloud.png",
                      "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]

            images_path = [images[condition]for condition in sky_condition]
            st.image(images_path, width=115)
    except KeyError:
       st.write("That place does not exist")
