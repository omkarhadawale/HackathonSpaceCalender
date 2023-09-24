import streamlit as st
import datetime
import json
import requests
from streamlit_calendar import calendar
import config
import numpy as np
import base64

custom_css = """
<style>
/* Set the content width to 100% */
.stApp {
    max-width: 100% !important;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
response_news = requests.get(config.URL_NEWS)
json_data_news = json.loads(response_news.text)
col1, col2 = st.columns(2)
results=json_data_news['results']

with col1:
    st.header("Articles")
    for article in results:
    
        expander = st.expander(article['title'])
        expander.write(article['summary'])
        expander.image(article['image_url'])
response_blog = requests.get(config.URL_BLOGS)
json_data_blog = json.loads(response_blog.text)
results=json_data_blog['results']

with col2:
    st.header("Blogs")
    for blogs in results:
    
        expander = st.expander(blogs['title'])
        expander.write(blogs['summary'])
        expander.image(blogs['image_url'])
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url({image_url});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
image_url = 'https://cdn.bhdw.net/im/space-explosion-wallpaper-28107_w635.webp'
set_bg_hack_url()

