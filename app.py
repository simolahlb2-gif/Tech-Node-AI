import streamlit as st
import google.generativeai as genai

# تم تحديث المحرك ليعمل بذكاء حقيقي وبدون تكرار
genai.configure(api_key="AIzaSyBorP4owFBWyopSg7BuvksYieoQKwLoeQ8")
model = genai.GenerativeModel('gemini-pro')

st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي الحقيقي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    try:
        # هنا سيمي يولد رداً جديداً تماماً في كل مرة
        res = model.generate_content(f"أنت سيمي، رد كإنسان ذكي وحر ومختصر جداً على: {p}")
        response_text = res.text
        with st.chat_message("assistant"):
            st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
    except:
        st.error("سيمي يواجه ضغطاً، حاولي مرة أخرى.")
