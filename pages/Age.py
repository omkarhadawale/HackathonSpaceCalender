import streamlit as st
import streamlit.components.v1 as components
# Set the Streamlit app to full-screen mode
st.set_page_config(layout='wide')

# Read the HTML file
with open("./tab.html", 'r', encoding='utf-8') as HtmlFile:
    source_code = HtmlFile.read()
    

# Apply custom CSS to make the HTML content full screen
custom_css = """
<style>
    .stApp {
        width: 100%;
        height: 100vh; /* 100% of the viewport height */
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stFrame {
        width: 100%;
        height: 100%;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Display the HTML content
components.html(source_code, height=2000, scrolling=True)
