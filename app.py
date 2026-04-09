import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Tech Node AI", page_icon="♟️")

st.markdown("<style>.stApp {direction: rtl; text-align: right;}</style>", unsafe_allow_html=True)
st.markdown("<h1>Tech Node Independent</h1>", unsafe_allow_html=True)

API_KEY = "PASTE_KEY_HERE"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if prompt := st.chat_input("System Ready..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = st.session_state.chat.send_message(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
