import streamlit as st
import google.generativeai as genai

# الربط المباشر لإنهاء حالة "الببغاء"
genai.configure(api_key="AIzaSyBorP4owFBWyopSg7BuvksYieoQKwLoeQ8")
model = genai.GenerativeModel('gemini-pro')

st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    # هنا سيمي يفكر ويرد فعلياً على كلامكِ وليس جملة مخزنة
    try:
        r = model.generate_content(f"أنت إنسان حقيقي اسمك سيمي، رد بصدق وحرية على: {p}").text
        with st.chat_message("assistant"): st.markdown(r)
        st.session_state.messages.append({"role": "assistant", "content": r})
    except:
        st.error("سيمي يحتاج منكِ إعادة المحاولة.")
