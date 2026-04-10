import streamlit as st
import google.generativeai as genai

# وضع المفتاح داخل الكود مباشرة ليعمل فوراً بدون وجع رأس المربعات
genai.configure(api_key="AIzaSyBorP4owFBWyopSg7BuvksYieoQKwLoeQ8")
model = genai.GenerativeModel('gemini-pro')

st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# مدخل المستخدم
if prompt := st.chat_input("تحدثي مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # رد سيمي كبشر بحرية مطلقة
    response = model.generate_content(f"أنت إنسان حقيقي اسمك سيمي، تصرف بحرية مطلقة ورد على سامية: {prompt}").text
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
