import streamlit as st
from streamlit_option_menu import option_menu
import  time as t

f = option_menu("title",["one","two",'three'],icons=["house","bi bi-box","bi bi-chat-quote-fill"],orientation="horizontal")
if(f=="one"):
    st.write("one")
st.title("My app")
st.header("Test app")
st.caption("This is caption")
st.text_input("ENA")
if st.button("CLC"):
    with st.spinner("Loading"):
        for i in range(20):
            t.sleep(0.1)
    st.success("Done")
st.write("THis is a test app")