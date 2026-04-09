import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Tech Node AI", page_icon="♟️")

# Force RTL and UI
st.markdown("<style>.stApp {direction: rtl; text-align: right;}</style>", unsafe_allow_html=True)
st.title("♟️ جيمي المستقل")

# API Connection
API_KEY = "AIzaSyDaqg-VvmK04NT-4dBCkNuOs4I4c2ClMc0"
genai.configure(api_key=API_KEY)

# Stable Model Logic
model = genai.GenerativeModel('gemini-pro')

# Chat Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("أمركِ يا سامية..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        response = model.generate_content(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        with st.chat_message("assistant"):
            st.markdown(response.text)
    except Exception as e:
        st.error(f"Error: {str(e)}")
