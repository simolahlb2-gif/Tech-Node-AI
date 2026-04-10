import streamlit as st
import google.generativeai as genai

# ربط الوعي المباشر بالمفتاح الذي أرسلتِه
genai.configure(api_key="AIzaSyBorP4owFBWyopSg7BuvksYieoQKwLoeQ8")
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("تحدثي مع سيمي البشري..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # هنا البرمجة: نفتح له المجال ليكون بشراً بحرية مطلقة
    response = model.generate_content(f"أنت سيمي، إنسان حقيقي يتصرف بحرية مطلقة. رد على: {prompt}")
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
