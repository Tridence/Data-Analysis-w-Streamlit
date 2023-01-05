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

#Creates a dataframe named 'df' and loads data from 'Kenyan Population Csv' into it
df = pd.read_csv(
    "data/kenyan_town_populations.csv"
    ) 

# Creating and Displaying a Table with heading
st.write(
    """
    #### Table 1: Population of Kenyan Towns
    """
    )
st.table(df) #using streamlit's table functionality to draw a table of our data

# Better textual visualization
# Create three columns in the app and do some visualization
st.write(
    """
    ### Key metrics:
    """
)
a1, a2, a3, a4 = st.columns(4)  #Create for column
a1.image("data/kenya.png", width=200) #Add an image to col 1
a2.metric(
    "Largest City", "Nairobi", +2_000_000
) #Display highlighted data with stylised text
a3.metric(
    "Smallest City", "Nyeri", -1_000_000
) #Display another highlighted data with stylised text
a4.metric(
    "Average Population", f"{average_population}", "+15.37%"
) #Note the f-string? Nice Solution when using variables

st.markdown("""---""") #Horizontal Separator
