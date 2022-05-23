import main_GUI
import Stocks_forcast
import Crypto_forcast
import about
from PIL import Image

import time
from streamlit_option_menu import option_menu
import streamlit as st
page_img = Image.open("img_src/page_icon.png")
PAGE_config = {"page_title": 'INVESTO',
               "page_icon": page_img, "layout": "centered"}
st.set_page_config(**PAGE_config)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: visible;}
            header {visibility: hidden;}
            footer:after{
                content : '             *******Made by Abhishek & Tanish ©️ 2022***********';
            
            }
            </style>
            
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


with st.sidebar:
    sel = option_menu(
        menu_title="Main Menu",
        options=["Crypto Quick View", "Stocks Overview & Prediction",
                 "Crypto detailed Overview and Prediction", "About us"],
        icons=["graph-up-arrow", "graph-up-arrow",
               "graph-up-arrow", "graph-up-arrow"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical"

    )

placeholder = st.empty()
if sel == "Crypto Quick View":
    st.sidebar.title(f"Current Selection :: {sel}")
    placeholder = main_GUI.app()


if sel == "Stocks Overview & Prediction":
    st.sidebar.title(f"Current Selection :: {sel}")
    placeholder = Stocks_forcast.app()


if sel == "Crypto detailed Overview and Prediction":
    st.sidebar.title(f"Current Selection :: {sel}")
    placeholder = Crypto_forcast.app()


if sel == "About us":
    st.sidebar.title(f"Current Selection :: {sel}")
    placeholder = about.app()


st.info("Made by Abhishek & Tanish ©️ 2022")
