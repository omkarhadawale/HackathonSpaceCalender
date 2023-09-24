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
        'date': '2020-01-05'
    }

    response = requests.get(config.URL,params=params)

    json_data = json.loads(response.text)

    image_url = json_data['url']

    image_title = json_data['title']
    image_desc = json_data['explanation']


    width = 350
    height = 150
    st.write(
        f'<link rel="preconnect" href="https://fonts.googleapis.com">'
        f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        f'<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&display=swap" rel="stylesheet">'
    f'''<div style="position: fixed; top: 20%; left: 50%; transform: translate(-50%, -50%); background-color: rgb(0,0,0,0.5); padding: 10px; font-family:'Caveat', 'cursive';font-size: 45px; font-weight: bold; color: white; text-align: center;">Image of the Day</div>''',
    unsafe_allow_html=True
    )

    st.write(
        f'<div id="blackBox" style="background-color: rgb(0,0,0,0.7); padding: 10px; color: white; position: fixed; bottom: 0; right: 0;">'
        f'<div style="font-weight: bold;text-align:center;font-size:20px">{image_title}</div>'
        f'<div style="font-size:16px;text-align:center">{image_desc}</div>'
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
