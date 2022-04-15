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

st.markdown("<h1 style='text-align: center; color: coral;'>🐟 Animal Crossing Fishpedia! 🐟</h1>", unsafe_allow_html=True)
st.markdown("<p class='short-font'>A comprehensive resource of all of the "
            "fish available in Animal Crossing: New Horizons </p>", unsafe_allow_html=True)


#st.write(fish)

hemispheres = ["Northern", "Southern"]
fish_hemisphere = st.radio("Which hemisphere do you play on?", hemispheres, index=0)

def fish_data():
    choice = st.checkbox("Check here to input a specific fish ID!", key=0)
    if choice:
        entry_no = st.number_input("Which fish are you looking for?", min_value=1, max_value=80, value=1, format='%d')
        if(entry_no):
            fishAPI = "http://acnhapi.com/v1/fish/" + str(entry_no)
            fish = requests.get(fishAPI).json()

            st.write("Essential " + str(fish["name"]["name-USen"]) + " information")
            st.write(fish)
            st.image(fish["icon_uri"])
            st.write("Regular Selling Price")
            st.write(str(fish["price"]) + " Bells")
            st.write("CJ's Offer")
            st.write(str(fish["price-cj"]) + " Bells")
            result = st.button("Additional Fish Information")
            if result:
                df = pd.DataFrame(
                    fish["name"],
                    index=["Names"])

                st.success("Enjoy your fish data!")
                st.dataframe(df)
                st.write("Fish Shadow Size in Water: ", fish["shadow"])
                st.image(fish["image_uri"], caption=fish["catch-phrase"])
                st.write(fish["museum-phrase"])



if fish_hemisphere == "Northern":
    nh = pd.DataFrame(
        np.random.randn(1000, 2) / [45, 45] + [45, 0],
        columns=['lat', 'lon']
    )
    st.map(nh, zoom=None)
    fish_data()
else:
    st.success("SOUTH")
    sh = pd.DataFrame(
        np.random.randn(1000, 2) / [45, 45] + [-45, 0],
        columns=['lat', 'lon']
    )
    st.map(sh, zoom=None)
    fish_data()

