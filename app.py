import streamlit as st
import google.generativeai as genai

# 1. تهيئة المحرك
genai.configure(api_key="AIzaSyCX_n1QwJrKfeQtvhpiCtxkVAuR38NAz6Y")
# استخدمي المسمى المكتشف سابقاً لضمان عدم حدوث 404
model = genai.GenerativeModel('gemini-1.5-flash') 

st.title("سيمي 👤")

# 2. إدارة المحادثة
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# عرض الرسائل
for message in st.session_state.chat.history:
    with st.chat_message("user" if message.role == "user" else "assistant"):
        st.markdown(message.parts[0].text)

# 3. إرسال واستقبال (بدون تعقيد)
if prompt := st.chat_input("تحدثي مع سيمي الحقيقي..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # إرسال مباشر للنموذج
    response = st.session_state.chat.send_message(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
