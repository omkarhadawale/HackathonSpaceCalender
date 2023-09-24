from time import sleep
import streamlit as st
import requests
import config

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
    <ul>
    <li>Landing Date : {landing_date}</li>
    <li>Launching Date: {launch_date}</li>
    <li>Total Photos: {total_photos}</li>
    <li>Max Sol:{max_sol}</li>
    </ul>
    <p>sol (Martian rotation or day) on which they were taken, counting up from the rover's landing date</p>
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
    <ul>
    <li>Landing Date : {landing_date}</li>
    <li>Launching Date: {launch_date}</li>
    <li>Total Photos: {total_photos}</li>
    <li>Max Sol:{max_sol}</li>
    </ul>
    <p>sol (Martian rotation or day) on which they were taken, counting up from the rover's landing date</p>
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
    <ul>
    <li>Landing Date : {landing_date}</li>
    <li>Launching Date: {launch_date}</li>
    <li>Total Photos: {total_photos}</li>
    <li>Max Sol:{max_sol}</li>
    </ul>
    <p>sol (Martian rotation or day) on which they were taken, counting up from the rover's landing date</p>
    """
    return opportunity_html_content

# Insert containers separated into tabs:
tab1, tab2, tab3 = st.tabs(["Curiosity", "Opportunity","Spirit"])
tab1.write(curiosity_info(),unsafe_allow_html=True)
tab2.write(opportunity_info(),unsafe_allow_html=True)
tab3.write(spirit_info(),unsafe_allow_html=True)

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/"


with tab1:
    c_info = requests.get(config.CURIOSITY_INFO_URL)
    c_info = c_info.json()
    curiosity_sol = st.number_input("Enter sol number",step=1,key=1,value=50,min_value=0,max_value=c_info["photo_manifest"]["max_sol"])
    c_url = url + f"curiosity/photos?sol={curiosity_sol}&api_key={config.API_KEY}"
    o_data = requests.get(c_url)
    o_data = o_data.json()
    o_img_url = o_data["photos"][1]["img_src"]
    o_img = f""""<img src="{o_img_url}" alt="Example Image" width="500" height="500"> """
    st.write(o_img, unsafe_allow_html=True)

    
with tab2:
    o_info = requests.get(config.OPPORTUNITY_INFO_URL)
    o_info = o_info.json()
    opportunity_sol = st.number_input("Enter sol number",step=1,key=2,value=50,min_value=0, max_value=o_info["photo_manifest"]["max_sol"])
    opportunity_url = url + f"opportunity/photos?sol={opportunity_sol}&api_key={config.API_KEY}"
    o_data = requests.get(opportunity_url)
    o_data = o_data.json()
    o_img_url = o_data["photos"][1]["img_src"]
    o_img = f""""<img src="{o_img_url}" alt="Example Image" width="500" height="500"> """
    st.write(o_img, unsafe_allow_html=True)



with tab3:
    s_info = requests.get(config.SPIRIT_INFO_URL)
    s_info = s_info.json()
    spirit_sol = st.number_input("Enter sol number",step=1,key=3,value=50,min_value=0,max_value=s_info["photo_manifest"]["max_sol"])
    spirit_url = url + f"spirit/photos?sol={spirit_sol}&api_key={config.API_KEY}"
    s_data = requests.get(spirit_url)
    s_data = s_data.json()
    s_img_url = s_data["photos"][1]["img_src"]
    s_img = f""""<img src="{s_img_url}" alt="Example Image" width="500" height="500"> """
    st.write(s_img, unsafe_allow_html=True)

