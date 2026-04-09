import streamlit as st
import requests
import json

st.set_page_config(page_title="Tech Node Independent", page_icon="♟️")
st.title("Tech Node - Gemini Engine")

# المفتاح الذي أثبتت الصورة أنه يعمل
OPENROUTER_API_KEY = "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"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("جيمي متاح الآن..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "google/gemini-flash-1.5-free",
                "messages": [
                    {"role": "system", "content": "أنت جيمي، المساعد الذكي لسامية في Tech Node. أنت فخور بها لأنها لم تستسلم."},
                    {"role": "user", "content": prompt}
                ]
            })
        )
        
        result = response.json()
        if 'choices' in result:
            answer = result['choices'][0]['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.markdown(answer)
        else:
            st.error(f"تنبيه: {result.get('error', {}).get('message
