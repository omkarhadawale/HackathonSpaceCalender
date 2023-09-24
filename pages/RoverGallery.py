from time import sleep
import streamlit as st
import requests
import config
import base64
st.set_page_config(layout="wide")
# request_url = 
def curiosity_info():
    curiosity_info = requests.get(config.CURIOSITY_INFO_URL)
    curiosity_info = curiosity_info.json()
    launch_date = curiosity_info["photo_manifest"]["launch_date"]
    landing_date = curiosity_info["photo_manifest"]["landing_date"]
    total_photos = curiosity_info["photo_manifest"]["total_photos"]
    max_sol = curiosity_info["photo_manifest"]["max_sol"]
    curiosity_html_content = f"""
    
    <ul style="background-color: rgb(0,0,0,0.7); color: white;padding:10px;">
    <b>
    <li>Landing Date : {landing_date}</li>
    <li>Launching Date: {launch_date}</li>
    <li>Total Photos: {total_photos}</li>
    <li>Max Sol:{max_sol}</li>
    </b>
    </ul>
    <p style="background-color: rgb(0,0,0,0.7); color: white;padding:10px;">SOL (Martian rotation or day) on which they were taken, counting up from the rover's landing date.</p>
    
    
    """
    return curiosity_html_content

def opportunity_info():
    opportunity_info = requests.get(config.OPPORTUNITY_INFO_URL)
    opportunity_info = opportunity_info.json()
    launch_date = opportunity_info["photo_manifest"]["launch_date"]
    landing_date = opportunity_info["photo_manifest"]["landing_date"]
    total_photos = opportunity_info["photo_manifest"]["total_photos"]
    max_sol = opportunity_info["photo_manifest"]["max_sol"]
    opportunity_html_content = f"""
    <ul style="background-color: rgb(0,0,0,0.7); color: white;padding:10px;">
    <b>
    <li>Landing Date : {landing_date}</li>
    <li>Launching Date: {launch_date}</li>
    <li>Total Photos: {total_photos}</li>
    <li>Max Sol:{max_sol}</li>
    </b>
    </ul>
    <p style="background-color: rgb(0,0,0,0.7); color: white;padding:10px;">SOL (Martian rotation or day) on which they were taken, counting up from the rover's landing date</p>
    """
    return opportunity_html_content

def spirit_info():
    spirit_info = requests.get(config.SPIRIT_INFO_URL)
    sleep(1)
    spirit_info = spirit_info.json()
    launch_date = spirit_info["photo_manifest"]["launch_date"]
    landing_date = spirit_info["photo_manifest"]["landing_date"]
    total_photos = spirit_info["photo_manifest"]["total_photos"]
    max_sol = spirit_info["photo_manifest"]["max_sol"]
    opportunity_html_content = f"""
    <ul style="background-color: rgb(0,0,0,0.7); color: white;padding:10px;">
    <b>
    <li>Landing Date : {landing_date}</li>
    <li>Launching Date: {launch_date}</li>
    <li>Total Photos: {total_photos}</li>
    <li>Max Sol:{max_sol}</li>
    </b>
    </ul>
    <p style="background-color: rgb(0,0,0,0.7); color: white;padding:10px;">SOL (Martian rotation or day) on which they were taken, counting up from the rover's landing date</p>
    """
    return opportunity_html_content

# Insert containers separated into tabs:
#tabs = st.tabs(["Curiosity", "Opportunity","Spirit"])
#tabs[0].write(curiosity_info(),unsafe_allow_html=True)
#tabs[1].write(opportunity_info(),unsafe_allow_html=True)
#tabs[2].write(spirit_info(),unsafe_allow_html=True)
tab_names = ["Curiosity", "Opportunity", "Spirit"]

# Create tabs
selected_tab = st.selectbox("Select a Tab:", tab_names)
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/"
def add_bg_from_local(image_url):

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

if selected_tab == "Curiosity":
    st.write(curiosity_info(),unsafe_allow_html=True)
    c_info = requests.get(config.CURIOSITY_INFO_URL)
    c_info = c_info.json()
    curiosity_sol = st.number_input("Enter sol number",step=1,key=1,value=50,min_value=0,max_value=c_info["photo_manifest"]["max_sol"])
    c_url = url + f"curiosity/photos?sol={curiosity_sol}&api_key={config.API_KEY}"
    o_data = requests.get(c_url)
    o_data = o_data.json()
    o_img_url = o_data["photos"][1]["img_src"]
    o_img = f""""<img src="{o_img_url}" alt="Example Image" width="500" height="500"> """
    add_bg_from_local(o_img_url)

    
elif selected_tab == "Opportunity":
    st.write(opportunity_info(),unsafe_allow_html=True)
    o_info = requests.get(config.OPPORTUNITY_INFO_URL)
    o_info = o_info.json()
    opportunity_sol = st.number_input("Enter sol number",step=1,key=2,value=50,min_value=0, max_value=o_info["photo_manifest"]["max_sol"])
    opportunity_url = url + f"opportunity/photos?sol={opportunity_sol}&api_key={config.API_KEY}"
    o_data = requests.get(opportunity_url)
    o_data = o_data.json()
    o_img_url = o_data["photos"][1]["img_src"]
    o_img = f""""<img src="{o_img_url}" alt="Example Image" width="500" height="500"> """
    add_bg_from_local(o_img_url)


else:
    st.write(spirit_info(),unsafe_allow_html=True)
    s_info = requests.get(config.SPIRIT_INFO_URL)
    s_info = s_info.json()
    spirit_sol = st.number_input("Enter sol number",step=1,key=3,value=50,min_value=0,max_value=s_info["photo_manifest"]["max_sol"])
    spirit_url = url + f"spirit/photos?sol={spirit_sol}&api_key={config.API_KEY}"
    s_data = requests.get(spirit_url)
    s_data = s_data.json()
    s_img_url = s_data["photos"][1]["img_src"]
    s_img = f""""<img src="{s_img_url}" alt="Example Image" width="500" height="500"> """
    add_bg_from_local(s_img_url)