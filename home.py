# Import the required libraries and modules
import os
import streamlit as st
from dotenv import load_dotenv

# Define paths
uploads_dir = "uploads"
tracker_file = "uploads/tracker.csv"

# Load environment variables from .env file
load_dotenv()

# Access the API token
api_token = os.getenv('HUGGING_FACE_API_TOKEN')

# Image directory setup
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

# Data tracker setup
if not os.path.exists(tracker_file):
    with open(tracker_file, 'w') as f:
        f.write("image_path,classification,timestamp,latitude,longitude,comment\n")
        
# Save the session state variables
st.session_state.uploads_dir = uploads_dir
st.session_state.tracker_file = tracker_file
st.session_state.api_token = api_token
        
# Create pages
upload_photo = st.Page("upload.py", title="Upload Photo", icon="📸")
reports_location = st.Page("location.py", title="Reports by Location", icon="📍")
trend_analysis = st.Page("trends.py", title="Trend Analysis", icon="📈")
summary_reports = st.Page("summary.py", title="Summary Reports", icon="📝")

# Create navigation menu on sidebar
menu = st.navigation([upload_photo, reports_location, trend_analysis, summary_reports], position="sidebar")
menu.run()

