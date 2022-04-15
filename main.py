import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title("Animal Crossing!")

fishAPI = "http://acnhapi.com/v1/fish/80"
fish = requests.get(fishAPI).json()
#st.write(fish)

hemispheres = ["Northern", "Southern"]
fish_hemisphere = st.radio("Which hemisphere do you play on?", hemispheres)

if fish_hemisphere == "Northern":
    st.success("NORTH")
    nh = pd.DataFrame(
        np.random.randn(1000, 2) / [45, 45] + [45, 0],
        columns=['lat', 'lon']
    )
    st.map(nh, zoom=None)
    choice = st.checkbox("Check here to input a specific fish ID!")
    if choice:
        entry_no = st.number_input("Which fish are you looking for?", min_value=1, max_value=80, value=1, format='%d')
        st.write("You have entered fish #", entry_no)

    #fish_option = st.selectbox("Choose the fish you're looking for!", )
else:
    st.success("SOUTH")
    sh = pd.DataFrame(
        np.random.randn(1000, 2) / [45, 45] + [-45, 0],
        columns=['lat', 'lon']
    )
    st.map(sh,zoom=None)
    choice = st.checkbox("Check here to input a specific fish ID!")
    if choice:
        entry_no = st.number_input("Which fish are you looking for?", min_value=1, max_value=80, value=1, format='%d')
        st.write("You have entered fish #", entry_no)
    #fish_option = st.selectbox("Choose the fish you're looking for!", )


result = st.button("Fish Encyclopedia")
if result:
    st.write("Success!")

