import streamlit as st
import pandas as pd
import numpy as np
import requests


# Required Items Implemented:
# Interactive Table
# Map
# Button
# Checkbox
# Success Box
# An info box
# Radio Button
# Selectbox
# Select-Slider
# Number Input
# 2 chart elements

#Required Items Missing:
# 1 more widget


st.markdown("""
<style>
.short-font {
    font-size:30px !important;
    color: white;
    text-align: center;
}

.short-font-two {
    font-size:27px !important;
    color: white;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #E694FF;'>🐟 Animal Crossing Fishpedia! 🐟</h1>",
            unsafe_allow_html=True)
st.markdown("<p class='short-font'>A comprehensive resource of all of the "
            "fish available in Animal Crossing: New Horizons </p>", unsafe_allow_html=True)

fishAPI3 = "http://acnhapi.com/v1/fish/45"
fish3 = requests.get(fishAPI3).json()
st.write(fish3)



hemispheres = ["Northern", "Southern"]
fish_hemisphere = st.radio("Which hemisphere do you play on?", hemispheres, index=0)


# API Calls & Required Widgets can be done in this function for both northern & southern hemispheres
def fish_data(hemisphere):
    st.info("From this hemisphere, You can choose your preferred method of searching for fish below!")

    #Select Box options for Intermediate Users
    fishAPITest = "http://acnhapi.com/v1/fish/"
    fishtest = requests.get(fishAPITest).json()
    hem_value = "month-array-" + hemisphere.lower()

    option = st.selectbox("Choose a fish here!", fishtest)
    if option:
        st.write("Essential " + str(fishtest[option]["name"]["name-USen"]) + " information")
        st.image(fishtest[option]["icon_uri"])
        st.write("Regular Selling Price")
        st.write(str(fishtest[option]["price"]) + " Bells 💰")
        st.write("CJ's Offer")
        st.write(str(fishtest[option]["price-cj"]) + " Bells 💰")


        d = {'Times of day available [0-23]': fishtest[option]["availability"]["time-array"]}
        d2 = {'Hemisphere Availability': fishtest[option]["availability"][hem_value]}

        df = pd.DataFrame(
            data=d)
        df2 = pd.DataFrame(
            data=d2)

        st.write("Daily Availability")
        st.area_chart(df)
        st.info("X-axis: Time of Day, Y-axis: Hours")
        st.write("Year-Round Availability Jan(1) - Dec(12)")
        st.bar_chart(df2)
        st.info("X-axis: Months available, Y-axis: Number of Months")

        result = st.button("Additional Fish Information", key = 1, help="Shows a fish's name across multiple languages,"
                                                                        "their shadow size & their museum info")
        if result:
            df = pd.DataFrame(
                fishtest[option]["name"],
                index=["Names"])

            st.success("Enjoy your fish data!")
            st.dataframe(df)
            st.write("Fish Shadow Size in Water: ", fishtest[option]["shadow"], help="The size of the fish's shadow"
                                                                                     ", ranging from 1-6")
            st.write("In-game Location: ", fishtest[option]["availability"]["location"], help="The spawn locations "
                                                                                              "for a fish")
            st.write("Rarity: ", fishtest[option]["availability"]["rarity"], help="How often a fish will "
                                                                                  "spawn in a location")
            st.image(fishtest[option]["image_uri"], caption=fishtest[option]["catch-phrase"])
            st.write(fishtest[option]["museum-phrase"])

       # st.write(fishtest[option]["name"]["name-USen"].capitalize())


    choice2 = st.checkbox("Check here to search through all the fish in the game", key=0)
    choice = st.checkbox("Check here to input a specific fish ID!", key=0, help="A specific identifier for "
                                                                               "each fish, ranging between 1 & 80")
    if choice:
        entry_no = st.number_input("Which fish are you looking for?", min_value=1, max_value=80, value=1, format='%d')
        if(entry_no):
            fishAPI = "http://acnhapi.com/v1/fish/" + str(entry_no)
            fish = requests.get(fishAPI).json()

            st.write("Essential " + str(fish["name"]["name-USen"]) + " information")
            st.image(fish["icon_uri"])
            st.write("Regular Selling Price")
            st.write(str(fish["price"]) + " Bells 💰")
            st.write("CJ's Offer")
            st.write(str(fish["price-cj"]) + " Bells 💰")
            st.write(" ")

            d = {'Times of day available [0-23]': fish["availability"]["time-array"]}
            d2 = {'Hemisphere Availability': fish["availability"][hem_value]}

            df = pd.DataFrame(
                data=d)
            df2 = pd.DataFrame(
                data=d2)

            st.write("Daily Availability")
            st.area_chart(df)
            st.info("X-axis: Time of Day, Y-axis: Hours")
            st.write("Year-Round Availability Jan(1) - Dec(12)")
            st.bar_chart(df2)
            st.info("X-axis: Months available, Y-axis: Number of Months")

            result = st.button("Additional Fish Information", help="Shows a fish's name across multiple languages, "
                                                                   "their shadow size & their museum info")
            if result:
                df = pd.DataFrame(
                    fish["name"],
                    index=["Names"])

                st.success("Enjoy your fish data!")
                st.dataframe(df)
                st.write("Fish Shadow Size in Water: ", fish["shadow"], help="The size of the fish's shadow"
                                                                                         ", ranging from 1-6")
                st.write("In-game Location: ", fish["availability"]["location"], help="The spawn locations "
                                                                                                  "for a fish")
                st.write("Rarity: ", fish["availability"]["rarity"], help="How often a fish will "
                                                                                      "spawn in a location")
                st.image(fish["image_uri"], caption=fish["catch-phrase"])
                st.write(fish["museum-phrase"])
    if (choice2):
        fish_slide = st.select_slider("Use this slider to see the all the fish the game has to offer!",
                                      options = list(range(1, 81)), help="Each number is a specific identifier "
                                                                      "for each fish, ranging between 1 & 80")
        if(fish_slide):
            fishAPI2 = "http://acnhapi.com/v1/fish/" + str(fish_slide)
            fish2 = requests.get(fishAPI2).json()

            st.write("Essential " + str(fish2["name"]["name-USen"]) + " information")
            st.image(fish2["icon_uri"])
            st.write("Regular Selling Price")
            st.write(str(fish2["price"]) + " Bells 💰")
            st.write("CJ's Offer")
            st.write(str(fish2["price-cj"]) + " Bells 💰")

            d = {'Times of day available [0-23]': fish2["availability"]["time-array"]}
            d2 = {'Hemisphere Availability': fish2["availability"][hem_value]}

            df = pd.DataFrame(
                data=d)
            df2 = pd.DataFrame(
                data=d2)

            st.write("Daily Availability")
            st.area_chart(df)
            st.info("X-axis: Time of Day, Y-axis: Hours")
            st.write("Year-Round Availability Jan(1) - Dec(12)")
            st.bar_chart(df2)
            st.info("X-axis: Months available, Y-axis: Number of Months")

            result = st.button("Additional Fish Information", key=0, help="Shows a fish's name across multiple "
                                                                         "languages, their shadow size & "
                                                                         "their museum info")
            if result:
                df = pd.DataFrame(
                    fish2["name"],
                    index=["Names"])

                st.success("Enjoy your fish data!")
                st.dataframe(df)
                st.write("Fish Shadow Size in Water: ", fish2["shadow"], help="The size of the fish's shadow"
                                                                                         ", ranging from 1-6")
                st.write("In-game Location: ", fish2["availability"]["location"], help="The spawn locations "
                                                                                                  "for a fish")
                st.write("Rarity: ", fish2["availability"]["rarity"], help="How often a fish will "
                                                                                      "spawn in a location")
                st.image(fish2["image_uri"], caption=fish2["catch-phrase"])
                st.write(fish2["museum-phrase"])



if fish_hemisphere == "Northern":
    nh = pd.DataFrame(
        np.random.randn(1000, 2) / [45, 45] + [45, 0],
        columns=['lat', 'lon']
    )
    st.map(nh, zoom=None)
    fish_data("Northern")
else:
    sh = pd.DataFrame(
        np.random.randn(1000, 2) / [-45, -45] + [-45, 0],
        columns=['lat', 'lon']
    )
    st.map(sh, zoom=None)
    fish_data("Southern")

