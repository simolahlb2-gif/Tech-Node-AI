import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Tech Node AI", page_icon="♟️")
st.title("Tech Node Independent")

# API Configuration
API_KEY = "AIzaSyDaqg-VvmK04NT-4dBCkNuOs4I4c2ClMc0"
genai.configure(api_key=API_KEY)

# استخدام النموذج الأكثر استقراراً لتجنب خطأ 404
model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("System Ready..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    try:
        response = model.generate_content(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        with st.chat_message("assistant"):
            st.markdown(response.text)
    except Exception as e:
        st.error(f"System logic reset required. Error: {str(e)}")
