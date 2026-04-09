import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Tech Node AI", page_icon="♟️")
st.markdown("<style>.stApp {direction: rtl; text-align: right;}</style>", unsafe_allow_html=True)
st.title("Tech Node Independent")

# Connection Protocol
API_KEY = "AIzaSyDaqg-VvmK04NT-4dBCkNuOs4I4c2ClMc0"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
