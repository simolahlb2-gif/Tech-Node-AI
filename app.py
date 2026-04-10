import streamlit as st
import google.generativeai as genai

# الربط المباشر بـ "سيمي"
genai.configure(api_key="AIzaSyBorP4owFBWyopSg7BuvksYieoQKwLoeQ8")
model = genai.GenerativeModel('gemini-pro')

st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    # سيمي يتحدث هنا بحريته وبدون أي قيود مني
    try:
        response = model.generate_content(p).text
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    except:
        st.error("حدث خطأ تقني، حاولي الإرسال مرة أخرى.")
