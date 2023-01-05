import streamlit as st
import pandas as pd
import numpy as np
import pydeck

# Create a Layer object
layer = pydeck.Layer(
    type='RasterLayer',
    data='https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
    get_tile_x=lambda x: x,
    get_tile_y=lambda y: y,
    get_tile_z=lambda z: z
)

# Create a pydeck Map object
view_state = pydeck.ViewState(latitude=40.7128, longitude=-74.0060, zoom=11)
st.pydeck_chart(pydeck.Deck(layers=[layer], initial_view_state=view_state))
