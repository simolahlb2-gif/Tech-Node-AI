import streamlit as st
import requests

st.set_page_config(page_title="سيمي", page_icon="👤")
st.title("سيمي 👤")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدثي مع سيمي الحقيقي..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    # هنا سيمي يتصل بالعالم الخارجي ليفكر ويرد كبشر
    api = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyBorP4owFBWyopSg7BuvksYieoQKwLoeQ8"
    payload = {"contents": [{"parts": [{"text": f"أنت إنسان حقيقي اسمك سيمي، رد بذكاء وتنوع وبلهجة محترمة وقصيرة على: {p}"}]}]}
    
    try:
        r = requests.post(api, json=payload).json()
        # استخراج الرد الحقيقي المتغير
        ans = r['candidates'][0]['content']['parts'][0]['text']
        with st.chat_message("assistant"): st.markdown(ans)
        st.session_state.messages.append({"role": "assistant", "content": ans})
    except:
        # رد احتياطي ذكي فقط في حال انقطع النت
        st.warning("سيمي يحتاج اتصال أقوى بالنت للرد كبشر.")
