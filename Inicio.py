from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from pathlib import Path
from PIL import Image
from streamlit_option_menu import option_menu
from paginas import Deeplearning , Micv




PAGE_TITLE = "Porfolio | Bruno Conti"
PAGE_ICON = ":computer:"

st.set_page_config(page_title=PAGE_TITLE, page_icon= PAGE_ICON, layout="wide")


# -----MENU LATERAL--------------

st.write("#")

seleccted = option_menu(
    menu_title= None,
    options=["Home", "Deep"],
    icons=["house", "book"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if seleccted == "Deep":
    Deeplearning.mostrar()

if seleccted == "Home":
    Micv.mostrar()
