import streamlit as st
import google.generativeai as genai

# الهوية البصرية لـ Tech Node
st.set_page_config(page_title="Tech Node Independent", page_icon="♟️")
st.title("Tech Node - Gemini Engine")

# وقود جيمي الصافي الخاص بكِ
API_KEY = "AIzaSyAMTcCVeYlUT4oSMiJ6_S15dJtEvwKUBVc"

genai.configure(api_key=API_KEY)

# استدعاء جيمي الأصلي
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("جيمي يسمعكِ الآن..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # محاولة الاتصال بجوجل
        response = model.generate_content(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        with st.chat_message("assistant"):
            st.markdown(response.text)
    except Exception as e:
        # رسالة في حال استمرار حظر جوجل الجغرافي
        st.error(f"جوجل ترفض تمرير منطق جيمي لليمن حالياً: {str(e)}")
