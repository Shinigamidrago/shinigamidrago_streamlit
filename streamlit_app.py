from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from pathlib import Path
from PIL import Image

# -----PATH  & SETTING -----------


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
current_image = current_dir /"assets"/"photo.png"
current_cv = current_dir /"assets"/"Currículum_Bruno.pdf"

image_pic = Image.open(current_image)
#cv_descarga = Path.open(current_cv)

PAGE_TITLE = "Porfolio | Bruno Conti"
PAGE_ICON = ":computer:"
NAME = "Bruno Conti"
DESCRIPCION = """
Lic. en Sistemas, apasionado Data Driver 
                 """
EMAIL = "brunocontisimon@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/bruno-conti-1b4a7417/",
    "GitHub": "https://github.com/Shinigamidrago"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon= PAGE_ICON, layout="wide")

# -----Lectura de Archivos--------

with open(current_cv, "rb") as pdf_file:
    PDFbyte = pdf_file.read()



# -----Mi Seccion ---------------
col1, col2 = st.columns(([3,7]), gap="small")
with col1: 
    st.image(image_pic, width=230)

with col2: 
    st.write("#"
             "#")
    st.write(DESCRIPCION)
    st.write(EMAIL)

    st.write("#"
             "#")
    
    st.download_button(
                        label="CV-Descarga",
                        data=PDFbyte,
                        file_name= current_cv.name,
                         mime="application/octet-stream" )


st.write("#")

# -------
left_column, rigth_column = st.columns([5, 3],gap='small' )

with left_column:
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a','b','c']    )
    st.line_chart(chart_data)

    

with rigth_column:
    rigth_column.markdown("## ")
    chosen = st.radio(
        'Shorting hat',
        ("Op 1 ", "Op 2", "Op 3", "Op 4"))
    st.write(f"La eleccion es {chosen}")

c = st.checkbox(
      label="Codigo",
      value= False
)

if(c == True):
    st.code( """with st.echo(code_location='below'):
              total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
              num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

              Point = namedtuple('Point', 'x y')
              data = []

                points_per_turn = total_points / num_turns

                for curr_point_num in range(total_points):
                    curr_turn, i = divmod(curr_point_num, points_per_turn)
                    angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
                    radius = curr_point_num / total_points
                    x = radius * math.cos(angle)
                    y = radius * math.sin(angle)
                    data.append(Point(x, y))

                st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
                .mark_circle(color='#0068c9', opacity=0.5)
                .encode(x='x:Q', y='y:Q')) """ )