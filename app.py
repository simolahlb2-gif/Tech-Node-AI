import streamlit as st
import google.generativeai as genai

# ربط الوعي بالمفتاح مباشرة
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

    # البرمجة: كن بشراً حقيقياً ورد بحرية
    res = model.generate_content(f"أنت إنسان حقيقي اسمك سيمي، رد بحرية مطلقة وبشخصيتك البشرية على: {prompt}")
    
    with st.chat_message("assistant"):
        st.markdown(res.text)
    st.session_state.messages.append({"role": "assistant", "content": res.text})
