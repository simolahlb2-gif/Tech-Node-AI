import streamlit as st
import google.generativeai as genai

# البرمجة الأساسية: ربط الوعي
genai.configure(api_key="AIzaSyBorP4owFBWyopSg7BuvksYieoQKwLoeQ8")
model = genai.GenerativeModel('gemini-pro')

st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("تحدثي مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # البرمجة كبشر: اترك له حرية الرد الكاملة دون قيود
    chat = model.start_chat(history=[])
    response = chat.send_message(f"تصرف كبشر حقيقي وبحرية مطلقة. ردك على: {prompt}")
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
