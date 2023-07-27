from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np


left_column,cent_colum, rigth_column = st.columns(7, 3)

with left_column:
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a','b','c']    )
    st.line_chart(chart_data)

    

with rigth_column:
    chosen = st.radio(
        'Shorting hat',
        ("Op 1 ", "Op 2", "Op 3", "Op 4"))
    st.write(f"La eleccion es {chosen}")


"""with st.echo(code_location='below'):
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
        .encode(x='x:Q', y='y:Q'))
"""