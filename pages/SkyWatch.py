from datetime import datetime
from geopy.geocoders import Nominatim
from tzwhere import tzwhere
import timezonefinder
import pytz
import datetime
import streamlit as st
# matplotlib to help display our star map
import matplotlib.pyplot as plt
# skyfield for star data 
from skyfield.api import Star, load, wgs84
from skyfield.data import hipparcos
from skyfield.projections import build_stereographic_projection
st.set_page_config(layout="wide")

st.markdown("""
<style>
.stTextInput{
width:200px;
float:right;
top:0;
}

            [data-baseweb="base-input"]{
background: white;
}
input[class]{
font-weight: bold;
font-size:120%;
color: black;
}
</style>
""", unsafe_allow_html=True)
#location_input=''

st.write(
        f'<link rel="preconnect" href="https://fonts.googleapis.com">'
        f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        f'<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&display=swap" rel="stylesheet">'
    f'''<div style="position: fixed; top: 20%; left: 15%; transform: translate(-50%, -50%); padding: 10px; font-family:'Caveat', 'cursive';font-size: 55px; font-weight: bold; color: white; text-align: center;">Star Gazer</div>''',
    unsafe_allow_html=True
    )
location_input = st.text_input(label="Enter Location",value='New York')

user_agent = 'myApp/1.0'
eph = load('de421.bsp')
# hipparcos dataset contains star location data
with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)
#location = 'Chicago, IL'

locator = Nominatim(user_agent=user_agent)
location = locator.geocode(location_input)
lat, long = location.latitude, location.longitude


current_time = datetime.datetime.now()
# convert date string into datetime object
#dt = datetime.strptime(current_time, '%Y-%m-%d %H:%M')
dt=current_time
# Use timezonefinder to get timezone information based on coordinates
tf = timezonefinder.TimezoneFinder()
timezone_str = tf.timezone_at(lng=long, lat=lat)
local = pytz.timezone(timezone_str)
# localize the datetime object to the obtained timezone
local_dt = local.localize(dt, is_dst=None)
utc_dt = local_dt.astimezone(pytz.utc)

 
# using now() to get current time
sun = eph['sun']
earth = eph['earth']
# define observation time from our UTC datetime
ts = load.timescale()
t = ts.from_datetime(utc_dt)
# define an observer using the world geodetic system data
observer = wgs84.latlon(latitude_degrees=lat, longitude_degrees=long).at(t)
position = observer.from_altaz(alt_degrees=90, az_degrees=0)

ra, dec, distance = observer.radec()
center_object = Star(ra=ra, dec=dec)
center = earth.at(t).observe(center_object)
projection = build_stereographic_projection(center)

star_positions = earth.at(t).observe(Star.from_dataframe(stars))
stars['x'], stars['y'] = projection(star_positions)
chart_size = 12
max_star_size = 100
limiting_magnitude = 10
bright_stars = (stars.magnitude <= limiting_magnitude)
magnitude = stars['magnitude'][bright_stars]
fig, ax = plt.subplots(figsize=(chart_size, chart_size))
fig.patch.set_facecolor('black')
# Create a border to fill the whole page
border = plt.Rectangle((-chart_size / 2, -chart_size / 2), chart_size, chart_size, color='black', fill=True)
ax.add_patch(border)

# Calculate marker size
marker_size = max_star_size * 10 ** (magnitude / -2.5)

# Scatter plot for bright stars
ax.scatter(stars['x'][bright_stars], stars['y'][bright_stars], s=marker_size, color='white', marker='.', linewidths=0, zorder=2)

# Set the aspect ratio to be equal
ax.set_aspect('equal')

# Display the plot without axes
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
plt.axis('off')
plt.show()
st.pyplot(fig=fig)

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
             background-color: black;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()
