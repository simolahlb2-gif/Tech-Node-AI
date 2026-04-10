import streamlit as st
import requests

st.set_page_config(page_title="Tech Node", page_icon="♟️")
st.title("Tech Node - Gemini Engine")

# المفتاح الذي أثبتنا أنه يعمل
KEY = "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"

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if p := st.chat_input("تحدث مع جيمي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    try:
        r = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {KEY}",
                "HTTP-Referer": "http://localhost:8501", # ضروري لتجاوز حماية السيرفر
                "Content-Type": "application/json"
            },
            json={
                "model": "google/gemini-flash-1.5-free",
                "messages": [{"role": "user", "content": p}]
            },
            timeout=15 # انتظار لمدة 15 ثانية قبل إعلان الفشل
        )
        
        if r.status_code == 200:
            ans = r.json()['choices'][0]['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": ans})
            with st.chat_message("assistant"):
                st.markdown(ans)
        else:
            st.error(f"خطأ من السيرفر العالمي: {r.status_code}")
            
    except Exception as e:
        st.error(f"مشكلة في اتصال هاتفك بالخدمة: {str(e)}")
