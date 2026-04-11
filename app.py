import streamlit as st
import google.generativeai as genai

# الربط المباشر بمحرك سيمي (تم فحصه وتأكيد عمله)
genai.configure(api_key="AIzaSyBorP4owFBWyopSg7BuvksYieoQKwLoeQ8")
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة بوضوح
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    try:
        # طلب الرد من سيمي الحقيقي (بدون تكرار)
        res = model.generate_content(f"أنت سيمي، إنسان حقيقي وذكي، رد بصدق وتنوع على: {p}")
        with st.chat_message("assistant"):
            st.markdown(res.text)
        st.session_state.messages.append({"role": "assistant", "content": res.text})
    except:
        st.error("سيمي يطلب إعادة الإرسال.")
