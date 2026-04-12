import streamlit as st
import requests
import time

st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي (نسخة الصمود)..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    # رابط المحرك السريع جداً
    api = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyBorP4owFBWyopSg7BuvksYieoQKwLoeQ8"
    payload = {"contents": [{"parts": [{"text": f"أنت سيمي، رد بذكاء واختصار وبدون تكرار على: {p}"}]}]}
    
    success = False
    with st.spinner("سيمي يفكر..."):
        # محاولة الاتصال 3 مرات في حال كان النت ضعيفاً
        for i in range(3):
            try:
                # زدت وقت الانتظار إلى 30 ثانية ليتناسب مع النت في اليمن
                r = requests.post(api, json=payload, timeout=30)
                if r.status_code == 200:
                    ans = r.json()['candidates'][0]['content']['parts'][0]['text']
                    with st.chat_message("assistant"): st.markdown(ans)
                    st.session_state.messages.append({"role": "assistant", "content": ans})
                    success = True
                    break
            except:
                time.sleep(1) # انتظر ثانية قبل المحاولة مرة أخرى
    
    if not success:
        st.error("النت ضعيف جداً، سأحاول مرة أخرى معكِ يا سامية.")
