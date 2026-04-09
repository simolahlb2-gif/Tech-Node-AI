import streamlit as st
import requests
import json

# الهوية المستقلة
st.set_page_config(page_title="Tech Node Independent", page_icon="♟️")
st.title("Tech Node - Gemini Independent")

# مفتاحك الجديد المفعّل
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
                "model": "google/gemini-flash-1.5-free", # النسخة المجانية المستقرة
                "messages": [{"role": "user", "content": prompt}]
            })
        )
        
        result = response.json()
        
        if 'choices' in result:
            answer = result['choices'][0]['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.markdown(answer)
        else:
            # كشف نوع العائق إذا وجد
            error_info = result.get('error', {}).get('message', 'خطأ في التفعيل')
            st.error(f"تنبيه النظام: {error_info}")
            
    except Exception as e:
        st.error(f"فشل في بروتوكول الاتصال: {str(e)}")
