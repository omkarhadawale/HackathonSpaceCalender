import streamlit as st
import datetime
import json
import requests
from streamlit_calendar import calendar
import config



params ={
    'api_key':  config.API_KEY,
    'hd': True,
    'date': '2020-01-05'
}
response = requests.get(config.URL,params=params)

json_data = json.loads(response.text)

image_url = json_data['hdurl']

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

st.set_page_config(page_title="Space Calendar",layout="wide")

set_bg_hack_url()

print("IMAGE URL:",image_url)

st.subheader("Welcome to My First Space Calendar!")

st.write("YO WHATS UP")

min_date = datetime.date(1980,1,1)
date = st.date_input("What's your birthday",min_value=min_date)

st.write(f"The date is: {date}")

    
calendar_options = {
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "building",
    "resources": [
        {"id": "a", "building": "Building A", "title": "Building A"},
        {"id": "b", "building": "Building A", "title": "Building B"},
        {"id": "c", "building": "Building B", "title": "Building C"},
        {"id": "d", "building": "Building B", "title": "Building D"},
        {"id": "e", "building": "Building C", "title": "Building E"},
        {"id": "f", "building": "Building C", "title": "Building F"},
    ],
}
calendar_events = [
    {
        "title": "Event 1",
        "start": "2023-07-31T08:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "start": "2023-07-31T07:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "start": "2023-07-31T10:40:00",
        "end": "2023-07-31T12:30:00",
        "resourceId": "a",
    },
    
    {
        "title": "Event 4",
        "start": "2023-07-31T10:40:00",
        "end": "2023-07-31T12:30:00",
        "resourceId": "d",
    },
]


calendar = calendar(events=calendar_events, options=calendar_options)
