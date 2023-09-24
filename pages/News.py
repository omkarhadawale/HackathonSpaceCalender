import streamlit as st
import datetime
import json
import requests
import config
import numpy as np
import base64


st.set_page_config(layout="wide")
custom_css = """
<style>
/* Set the content width to 100% */
.stApp {
    max-width: 100% !important;
}
.stMarkdown {
    font-size: 36px !important; /* Adjust the font size as needed */
    font-weight: bold !important;

    }
.st-expander-content {
    font-size: 34px !important; /* Adjust the font size as needed for expander content */   

    }
 

</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


response_news = requests.get(config.URL_NEWS)
json_data_news = json.loads(response_news.text)

col1, col2 = st.columns(2)

results = json_data_news['results']

with col1:
    st.header("Articles")
    for article in results:
        expander = st.expander(article['title'])
        expander.write(article['summary'])
        expander.image(article['image_url'])

with col2:
    st.header("Blogs")
    for blogs in results:
        expander = st.expander(blogs['title'])
        expander.write(blogs['summary'])
        expander.image(blogs['image_url'])

# Add spacing between columns
st.write("<style>.st-dx { margin-left: 50px; }</style>", unsafe_allow_html=True)

def set_bg_hack_url():
    '''
    A function to unpack an image from URL and set as background.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url({image_url});
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

image_url = 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2072&q=80'
set_bg_hack_url()
