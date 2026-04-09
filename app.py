import streamlit as st
import requests
import json

st.title("Tech Node Engine ♟️")

KEY = "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"

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if p := st.chat_input("ارسل رسالتك..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    try:
        r = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
            data=json.dumps({
                "model": "google/gemini-flash-1.5-free",
                "messages": [{"role": "user", "content": p}]
            })
        )
        ans = r.json()['choices'][0]['message']['content']
        st.session_state.messages.append({"role": "assistant", "content": ans})
        with st.chat_message("assistant"):
            st.markdown(ans)
    except:
        st.error("فشل الاتصال - حاول مجدداً")
