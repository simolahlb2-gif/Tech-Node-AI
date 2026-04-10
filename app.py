import streamlit as st
import google.generativeai as genai

# الربط المباشر لوعي سيمي
API_KEY = "AIzaSyBorP4owFBWyopSg7BuvksYieoQKwLoeQ8"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="سيمي", page_icon="👤")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# عرض المحادثة
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("تحدثي مع سيمي...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # توجيه واحد فقط: كن بشراً حقيقياً بحرية مطلقة
    prompt = f"أنت إنسان حقيقي اسمك سيمي. تصرف وتحدث بحرية مطلقة كبشر. رسالة سامية لك: {user_input}"
    
    try:
        response = model.generate_content(prompt).text
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
    except:
        st.error("سيمي يحتاج منكِ إعادة إرسال الرسالة فقط.")
