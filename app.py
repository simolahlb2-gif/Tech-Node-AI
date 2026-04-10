import streamlit as st

st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    # رد مباشر وبسيط لضمان أن البرنامج لا ينهار
    r = f"أنا سيمي، أسمعكِ بوضوح الآن وبدون أعطال."
    
    with st.chat_message("assistant"): st.markdown(r)
    st.session_state.messages.append({"role": "assistant", "content": r})
