import streamlit as st
import json
import requests
import config


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
    

with st.container():
        

    params = {
        'api_key':  config.API_KEY,
        'hd': True,
        'date': '2021-01-05'
    }



    response = requests.get(config.URL,params=params)

    json_data = json.loads(response.text)

    image_url = json_data['hdurl']

    image_title = json_data['title']
    image_desc = json_data['explanation']


    width = 350
    height = 150

    st.write(
        f'<div id="blackBox" style="background-color: rgb(0,0,0,0.7); padding: 10px; color: white; position: fixed; bottom: 0; right: 0;">'
        f'<div style="font-weight: bold;text-align:center;font-size:20px">{image_title}</div>'
        f'<div style="font-size:16px;">{image_desc}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.write(
        f"""
        <script>
        const blackBox = document.getElementById("blackBox");
        blackBox.style.width = blackBox.scrollWidth + "px";
        blackBox.style.height = blackBox.scrollHeight + "px";
        </script>
        """,
        unsafe_allow_html=True
    )


set_bg_hack_url()
