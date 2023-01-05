"""
A simple streamlit app demo
"""

import streamlit as st #Import the streamlit package to the app
import pandas as pd #Import the pandas package to handle data

#Page setting - Set's your application's layout, title and icon
#"KE" is the shortcode for an emoji of the Kenyan Flag
#Check all supported emojis here - https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json

st.set_page_config(
    layout="wide", page_title="Visualising City Population, Kenya", page_icon="🇰🇪"
)

# The code below use the inbuilt streamlit "write" functionality and 
# Markdown Language to write formated texts on your app
# You can learn more about Markdown by googling it

st.write(
    """
    ## My first streamlit application
    ### This app will display graphs of the populations of several kenya towns
    """
)