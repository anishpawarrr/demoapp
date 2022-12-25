import streamlit as st
from streamlit_option_menu import option_menu
import time as t
import pandas as pd
import plotly_express as px
import requests
def get_location(ip_address):
  # Make a request to the geolocation service with the IP address
  response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=eca3fc42a0c34ee8b745ebc67042795a&ip={ip_address}')

  # Check if the request was successful
  if response.status_code == 200:
    # Get the location data from the response
    location_data = response.json()

    # Extract the location information from the data
    country = location_data.get('country_name')
    city = location_data.get('city')
    latitude = location_data.get('latitude')
    longitude = location_data.get('longitude')

    # Return the location information
    return (country, city, latitude, longitude)
  else:
    # Return None if the request was not successful
    return None
st.set_page_config("set_page_config")
st.title("My ddrety app")
f = option_menu("Select",["one","two",'three'],icons=["house","bi bi-box","bi bi-chat-quote-fill"],orientation="horizontal")
if(f=="one"):
    st.write("one")
if(f=="two"):
    # st.write(map_)
    # l = (18.4577736, 73.8507165)
    # l = [[18.457773634234533465623423587639845634876394856932345345, 73.85071653526562345634524543245366758739447856238452347]]
    l = [[19.00643, 72.82194]]
    #'19.00643', '72.82194'
    l = pd.DataFrame(l, columns=['lat', 'lon'])
    st.pydeck_chart()
    fig = px.scatter_geo(data_frame=l, lat= 'lat', lon= 'lon', height=80)
    st.write(l)
    # df = pd.DataFrame(
    #     np.ndarray(l),
    #     columns=['lat', 'lon'])
    st.map(l)
    # st.plotly_chart(fig, use_container_width=True)
    # st.write(type(df))
    # st.pydeck_chart()



st.header("Test app")
st.caption("This is caption")
st.text_input("ENA")
if st.button("CLC"):
    with st.spinner("Loading"):
        for i in range(20):
            t.sleep(0.1)
    st.success("Done")
st.write("THis is a test app")