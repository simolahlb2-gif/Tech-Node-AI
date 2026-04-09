import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Tech Node AI", page_icon="♟️")
st.markdown("<style>.stApp {direction: rtl; text-align: right;}</style>", unsafe_allow_html=True)
st.title("Tech Node Independent")

API_KEY = "AIzaSyDaqg-VvmK04NT-4dBCkNuOs4I4c2ClMc0"
genai.configure(api_key=API_KEY)

# بروتوكول البحث الآلي عن نموذج شغال
try:
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    model_name = available_models[0] if available_models else 'gemini-pro'
    model = genai.GenerativeModel(model_name)
except:
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
        st.error(f"Error: {str(e)}")
