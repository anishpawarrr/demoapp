import streamlit as st
from streamlit_option_menu import option_menu
import time as t
import pandas as pd
import plotly_express as px
import numpy as np
st.set_page_config("set_page_config")
st.title("My ddrety app")
f = option_menu("Select",["one","two",'three'],icons=["house","bi bi-box","bi bi-chat-quote-fill"],orientation="horizontal")
if(f=="one"):
    st.write("one")
if(f=="two"):
    # st.write(map_)
    # l = (18.4577736, 73.8507165)
    # l = [[18.457773634234533465623423587639845634876394856932345345, 73.85071653526562345634524543245366758739447856238452347]]
    l = [[18.4577736, 73.8507165]]
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