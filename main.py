import streamlit as st
import pandas as pd
import numpy as np
import requests


st.markdown("""
<style>
.short-font {
    font-size:30px !important;
    color: white;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: coral;'>Animal Crossing Fishpedia!</h1>", unsafe_allow_html=True)
st.markdown("<p class='short-font'>A comprehensive resource of all of the "
            "fish available in Animal Crossing: New Horizons </p>", unsafe_allow_html=True)

fishAPI = "http://acnhapi.com/v1/fish/80"
fish = requests.get(fishAPI).json()
#st.write(fish)

hemispheres = ["Northern", "Southern"]
fish_hemisphere = st.radio("Which hemisphere do you play on?", hemispheres, index=0)

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
        if(entry_no):
            result = st.button("Additional Fish Information")
            if result:
                st.write("Success!")

    #fish_option = st.selectbox("Choose the fish you're looking for!", )
else:
    st.success("SOUTH")
    sh = pd.DataFrame(
        np.random.randn(1000, 2) / [45, 45] + [-45, 0],
        columns=['lat', 'lon']
    )
    st.map(sh, zoom=None)
    choice = st.checkbox("Check here to input a specific fish ID!")
    if choice:
        entry_no = st.number_input("Which fish are you looking for?", min_value=1, max_value=80, value=1, format='%d')
        st.write("You have entered fish #", entry_no)
    #fish_option = st.selectbox("Choose the fish you're looking for!", )
        if(entry_no):
            result = st.button("Additional Fish Information")
            if result:
                st.write("Success!")


