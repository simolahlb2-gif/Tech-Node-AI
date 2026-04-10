import streamlit as st
import requests

st.set_page_config(page_title="Tech Node", page_icon="♟️")
st.title("Tech Node - Gemini Engine")

if "MY_KEY" in st.secrets:
    KEY = st.secrets["MY_KEY"]
else:
    st.error("المفتاح غير موجود في Secrets!")
    st.stop()

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
                "Content-Type": "application/json",
            },
            json={
                "model": "google/gemini-2.0-flash-001", # الموديل الأكثر استقراراً في العالم حالياً
                "messages": [{"role": "user", "content": p}]
            }
        )
        
        if r.status_code == 200:
            ans = r.json()['choices'][0]['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": ans})
            with st.chat_message("assistant"):
                st.markdown(ans)
        else:
            st.error(f"تنبيه السيرفر العالمي: {r.json().get('error', {}).get('message', 'خطأ في التوفر')}")
            
    except Exception as e:
        st.error(f"عطل تقني: {str(e)}")
