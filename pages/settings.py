# settings.py
import streamlit as st
import json

st.set_page_config(page_title="Settings", page_icon="📈")

st.header("Settings")
st.write("Here you can adjust the settings for the app.")

# Auswahlmöglichkeit für die Trendsuchfunktion
st.subheader("Trend Search Engine")
st.session_state['trend_engine'] = st.selectbox(
    "Select Trend Search Engine",
    ("X", "GPT")
)

# Auswahlmöglichkeit für die Trendsuchfunktion
st.subheader("Video Generation Engine")
st.session_state['video_engine'] = st.selectbox(
    "Select Video Generation Engine",
    ("D-ID", "Heygen")
)

# API Key configurations
st.subheader("API Key Configurations")
st.session_state['TWITTER_BEARER_TOKEN'] = st.text_input("Twitter Bearer Token", type="password")
st.session_state['YOUR_OPENAI_API_KEY'] = st.text_input("OpenAI API Key", type="password")
st.session_state['HEYGEN_API_KEY'] = st.text_input("HeyGen API Key", type="password")
st.session_state['D_ID_API_KEY'] = st.text_input("D-ID API Key", type="password")

# Save button to persistently save the settings
if st.button("Save Settings"):
    settings_data = {
        'TWITTER_BEARER_TOKEN': st.session_state['TWITTER_BEARER_TOKEN'],
        'YOUR_OPENAI_API_KEY': st.session_state['YOUR_OPENAI_API_KEY'],
        'HEYGEN_API_KEY': st.session_state['HEYGEN_API_KEY'],
        'D_ID_API_KEY': st.session_state['D_ID_API_KEY'],
        'trend_engine': st.session_state['trend_engine'],
        'video_engine': st.session_state['video_engine']
    }
    
    with open("settings.json", "w") as f:
        json.dump(settings_data, f)
    
    st.success("Settings saved successfully!")